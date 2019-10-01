#!/usr/bin/python
import sys, os, os.path, urllib2, re, cookielib, time, datetime, locale

file = 'conv_rates.txt' #file containing the exchange rates

locale.setlocale( locale.LC_ALL, '' )

def check_file(file):
	#check that the file exists and it's not empty
	if os.path.exists(file) == False or os.stat(file).st_size == 0:
		grab_web_rates()

	#check that the file is no more than 24 hours old
	if  time.time() - os.path.getmtime(file) > 86400: #file older than 24 hours
		#grab the currency exchange data form the internet
		grab_web_rates()
	else: #file is up to date
		return create_exchange_dict()

def create_exchange_dict():
	exchange_rates_dict = {}
	conversion_rates = open (file, 'r') #open file read only

	for line in conversion_rates:
		exchange_rates_dict[line.split(",")[0]] = line.split(",")[1]

	conversion_rates.close()
	return exchange_rates_dict

def grab_web_rates():
	conversion_rates = open (file, 'w')
	web = urllib2.urlopen('http://www.x-rates.com/table/?from=USD')
	html = web.read()
	line = 1
	titles = re.findall(r'<td class=\'rtRates\'>
	<a href=\'/graph/\?from=(.*?)</td>', html)
	for title in titles:
		title = title.replace("amp;to=", "")
		title = title.replace("&", "-")
		title = title.replace("'>", ",")
		title = title.replace("</a>", " ")
		title = title.replace("  ", "")
		title = title.rstrip()
		conversion_rates.write(title + ' \n')
		line += 1
		if line >= 23:
			break
	conversion_rates.close()

def get_result(choice, amount):
	dict = create_exchange_dict()
	for exchange,rate in dict.items():
		if exchange == choice:
			result = amount * float(rate)
			return rate, result
			break
		else:
			error = "Exchange not found! -get_result()- "

def format_currency(value):
    return "{:,.2f}".format(value)

def checkChoice(choice):
	if str.isdigit(choice): #check that the selection is a digit or exit
		return True
	else:
		os.system('clear')
		print "Thanks for using Currency Calculator! \n"
		exit()

def main():
	os.system('clear')
	print '''
	Chose the Conversion:
	1. US Dollar -> Euro
	2. Euro -> US Dollar
	3. US Dollar -> British Pound
	4. British Pound -> US Dollar
	5. US Dollar -> Canadian Dollar
	6. Canadian Dollar -> US Dollar
	7. US Dollar -> Chines Yuan
	8. Chines Yuan -> US Dollar
	9. US Dollar -> Peso Argentino
	10. Peso Argentino -> US Dollar
	0. Exit
	'''
	choice = raw_input("\t")

	checkChoice(choice)
	choice = int(choice)

	#Exit script if the selection is not whithin the allowed range
	if choice == 0 or choice > 10:
		os.system('clear')
		print "Thanks for using Currency Calculator! \n"
		exit()

	while choice != 0:
		check_file(file)
		amount = raw_input("Amount: ")

		#Strips commas if found
		if ',' in amount:
			amount = ''.join(e for e in amount if e.isdigit() or e == '.')
			amount = float(amount)
		else:
			amount = float(amount)

		if choice == 1: #USD->Euro
			os.system('clear')
			choice = "USD-EUR"
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			e=u'\u20ac' #euro symbol
			amount = locale.currency( amount, grouping=True )
			print "Your amount (USD): ", amount
			print "Converts to (EUR): ", e, format_currency(result)
			print "The Euro (EUR) -> US Dollar exchange rate is: ", rate
			break

		elif choice  == 2: #EURO->USD
			os.system('clear')
			choice = "EUR-USD"
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			e=u'\u20ac' #euro symbol
			amount = format_currency(amount)
			print "Your amount (EUR): ", e, amount
			print "Converts to (USD): ", locale.currency(result, grouping=True)
			print "The US Dollar -> Euro (EUR) exchange rate is: ", rate
			break

		elif choice == 3: #GBP->USD
			choice = "USD-GBP"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			e = u'\xA3' #British Pound symbol
			amount = locale.currency( amount, grouping=True )
			print "Your amount (USD): ", amount
			print "Converts to (GBP): ", e, format_currency(result)
			print "The US Dollar -> British Pound (GBP) exchange rate is: ", rate
			break

		elif choice == 4: #USD->GBP
			choice = "GBP-USD"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			e = u'\xA3' #British Pound symbol
			amount = format_currency(amount)
			print "Your amount (GBP): ", e, amount
			print "Converts to (USD): ", locale.currency(result, grouping=True )
			print "The British Pound (GBP) -> US Dollar exchange rate is: ", rate
			break

		elif choice == 5: #CAD->USD
			choice = "USD-CAD"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			amount = locale.currency( amount, grouping=True )
			result = locale.currency( result, grouping=True )
			print "Your amount (USD): ", amount
			print "Converts to (CAD): ", result
			print "The US Dollar -> Canadian Dollar (CAD) exchange rate is: ", rate
			break

		elif choice == 6: #USD->CAD
			choice = "CAD-USD"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			amount = locale.currency( amount, grouping=True )
			result = locale.currency( result, grouping=True )
			print "Your amount (CAD): ", amount
			print "Converts to (USD): ", result
			print "The Canadian Dollar (CAD) -> US Dollar exchange rate is: ", rate
			break

		elif choice == 7: #USD->CNY
			choice = "USD-CNY"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			amount = locale.currency( amount, grouping=True )
			print "Your amount (CNY): ", amount
			print "Converts to Yuan (USD): " , format_currency(result)
			print "The US Dollar -> Chinese Yuan (CNY) exchange rate is: ", rate
			break

		elif choice == 8: #CNY->USD
			choice = "CNY-USD"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			print "Your amount (CNY): ", format_currency(amount)
			print "Converts to Yuan (USD): " , locale.currency( result, grouping=True )
			print "The Chinese Yuan (CNY) -> US Dollar exchange rate is: ", rate
			break

		elif choice == 9: #USD->ARS
			choice = "USD-ARS"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			amount = locale.currency( amount, grouping=True )
			print "Your amount (USD): ", amount
			print "Converts in Peso Argentino (ARS): " , format_currency(result)
			print "The US Dollar -> Peso Argentino (ARS) exchange rate is: ", rate
			break

		elif choice == 10: #ARS->USD
			choice = "ARS-USD"
			os.system('clear')
			r = get_result(choice, amount)
			result = r[1]
			rate = r[0]
			print "Your amount (ARS): ", format_currency(amount)
			print "Converts to US Dollar (USD): " , locale.currency(result, grouping=True)
			print "The Peso Argentino (ARS) -> US Dollar exchange rate is: ", rate
			break

		elif choice > 10:
			exit()
		break

#execution
main()
