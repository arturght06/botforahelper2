import sqlite3 as sq
from reqdata import req

def sql_start():
	global base, cur
	base = sq.connect('database/numbers.db')
	cur = base.cursor()
	base.execute('CREATE TABLE IF NOT EXISTS numbers(user_id, phone_number PRIMARY KEY, barcode, acstkn)')
	base.commit()
	if base:
		print('Data base connected OK!')
	

async def sql_add_number(userid, acstkn):
	request = req(acstkn)
	print(request)
	if request == False:
		return False
	phone_number = request['phone_number']
	barcode = request['barcode']
	print((userid, phone_number, barcode, acstkn))
	try:
		cur.execute('INSERT INTO numbers VALUES(?, ?, ?, ?)', (userid, phone_number, barcode, acstkn))
		base.commit()
	except:
		return 'FalseNumber'





async def sql_find_all_numbers(userid):
	all_nums = cur.execute('SELECT phone_number FROM numbers WHERE user_id == ?', (userid,)).fetchall()
	base.commit()
	return all_nums

async def sql_find_all_barcodes(userid):
	all_barcs = cur.execute('SELECT barcode FROM numbers WHERE user_id == ?', (userid,)).fetchall()
	base.commit()
	return all_barcs

async def sql_find_barcode(nums):
	all_barcs = cur.execute('SELECT barcode FROM numbers WHERE phone_number == ?', nums).fetchall()
	base.commit()
	return all_barcs

async def sql_find_acstkn(nums):
	acstkn = cur.execute('SELECT acstkn FROM numbers WHERE phone_number == ?', nums).fetchall()
	base.commit()
	return acstkn

async def delete_number(userid, phone_number):
	cur.execute('DELETE FROM numbers WHERE user_id == ? AND phone_number == ?', (userid, phone_number))