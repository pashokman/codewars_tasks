"""
The Coupon Code

Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False

"""
from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    parsed_current_date = datetime.strptime(current_date, '%B %d, %Y')
    parsed_expiration_date = datetime.strptime(expiration_date, '%B %d, %Y')

    if entered_code is correct_code and parsed_current_date <= parsed_expiration_date:
        return True
    else:
        return False


print(check_coupon('123','123','September 5, 2014','October 1, 2014'), True);
print(check_coupon('123a','123','September 5, 2014','October 1, 2014'), False);
print(check_coupon(0,False,'September 5, 2014', 'September 25, 2014'), False);
