from flask import Blueprint, render_template, request, redirect, session, url_for
from config.errors import Errors
from server.app import db
from database.tables.user import User
from database.tables.bills import Bill
from sqlalchemy.orm import joinedload

admin_bp = Blueprint("auth", __name__, template_folder="templates/auth")

@admin_bp.route("/admin/users", methods=["GET"])
def display_users():
    users = User.query.options(joinedload(User.preferences)).all()
    return render_template("users.html", users=users)

@admin_bp.route("/admin/bills", methods=["GET"])
def display_bills():
    bills = Bill.query.options(joinedload(Bill.actions)).all()
    return render_template("bills.html", bills=bills)