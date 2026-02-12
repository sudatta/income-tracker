import json
from datetime import date, timedelta
from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_required, current_user
from app import db
from models import JournalEntry
from forms import JournalEntryForm

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@login_required
def dashboard():
    today = date.today()

    # Weekly data: last 7 days
    week_start = today - timedelta(days=6)
    weekly_entries = (
        JournalEntry.query
        .filter_by(user_id=current_user.id)
        .filter(JournalEntry.date >= week_start, JournalEntry.date <= today)
        .order_by(JournalEntry.date)
        .all()
    )

    weekly_data = {
        "labels": [],
        "expenses": [],
        "income": [],
        "withdrawals": [],
        "net_income": [],
    }
    entries_by_date = {e.date: e for e in weekly_entries}
    for i in range(7):
        d = week_start + timedelta(days=i)
        weekly_data["labels"].append(d.strftime("%a %m/%d"))
        entry = entries_by_date.get(d)
        inc = entry.income if entry else 0
        exp = entry.expenses if entry else 0
        wdr = entry.withdrawals if entry else 0
        weekly_data["income"].append(inc)
        weekly_data["expenses"].append(exp)
        weekly_data["withdrawals"].append(wdr)
        weekly_data["net_income"].append(inc - (exp + wdr))

    # Monthly data: last 6 months
    monthly_data = {
        "labels": [],
        "expenses": [],
        "income": [],
        "withdrawals": [],
        "net_income": [],
    }
    for i in range(5, -1, -1):
        # Calculate month offset
        month = today.month - i
        year = today.year
        while month <= 0:
            month += 12
            year -= 1

        month_label = date(year, month, 1).strftime("%b %Y")
        monthly_data["labels"].append(month_label)

        # Get all entries for this month
        if month == 12:
            next_month_start = date(year + 1, 1, 1)
        else:
            next_month_start = date(year, month + 1, 1)
        month_start = date(year, month, 1)

        month_entries = (
            JournalEntry.query
            .filter_by(user_id=current_user.id)
            .filter(JournalEntry.date >= month_start, JournalEntry.date < next_month_start)
            .all()
        )

        total_inc = sum(e.income for e in month_entries)
        total_exp = sum(e.expenses for e in month_entries)
        total_wdr = sum(e.withdrawals for e in month_entries)
        monthly_data["income"].append(total_inc)
        monthly_data["expenses"].append(total_exp)
        monthly_data["withdrawals"].append(total_wdr)
        monthly_data["net_income"].append(total_inc - (total_exp + total_wdr))

    return render_template(
        "dashboard.html",
        weekly_data=json.dumps(weekly_data),
        monthly_data=json.dumps(monthly_data),
    )


@main_bp.route("/journal", methods=["GET", "POST"])
@login_required
def journal():
    form = JournalEntryForm()
    existing_entry = None

    if form.validate_on_submit():
        entry_date = form.date.data
        existing = JournalEntry.query.filter_by(
            user_id=current_user.id, date=entry_date
        ).first()

        # If entry exists and user confirmed update, or no existing entry
        if existing:
            if request.form.get("confirm_update") == "yes":
                existing.expenses = form.expenses.data or 0.0
                existing.income = form.income.data or 0.0
                existing.withdrawals = form.withdrawals.data or 0.0
                existing.notes = form.notes.data
                db.session.commit()
                flash(f"Entry for {entry_date} updated successfully.", "success")
                return redirect(url_for("main.journal"))
            else:
                # Show confirmation prompt
                existing_entry = existing
                flash(
                    f"An entry already exists for {entry_date}. "
                    "Review the existing values below and confirm to update.",
                    "warning",
                )
                return render_template(
                    "journal.html", form=form, existing_entry=existing_entry
                )
        else:
            entry = JournalEntry(
                user_id=current_user.id,
                date=entry_date,
                expenses=form.expenses.data or 0.0,
                income=form.income.data or 0.0,
                withdrawals=form.withdrawals.data or 0.0,
                notes=form.notes.data,
            )
            db.session.add(entry)
            db.session.commit()
            flash(f"Entry for {entry_date} saved successfully.", "success")
            return redirect(url_for("main.journal"))

    return render_template("journal.html", form=form, existing_entry=existing_entry)


@main_bp.route("/api/entry/<entry_date>")
@login_required
def get_entry(entry_date):
    try:
        d = date.fromisoformat(entry_date)
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    entry = JournalEntry.query.filter_by(user_id=current_user.id, date=d).first()
    if entry:
        return jsonify({
            "exists": True,
            "expenses": entry.expenses,
            "income": entry.income,
            "withdrawals": entry.withdrawals,
            "notes": entry.notes or "",
        })
    return jsonify({"exists": False})
