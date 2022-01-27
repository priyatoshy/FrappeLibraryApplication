# Copyright (c) 2022, Priyatosh and contributors
# For license information, please see license.txt

# import frappe

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from datetime import datetime


class Trancation(Document):

	def validate(self):
		self.check_database()



	def check_database(self):
		book_name=frappe.db.get_value('Books',self.book_name,'book_name')
		book_status=frappe.db.get_value('Books',self.book_name,'book_status')
		frappe.msgprint(_(f"Book: {book_name} Status: {book_status}"))
		if self.action_type.lower()=="issue":
			if book_status.lower()=='taken':
				frappe.msgprint(_(f"Book Unvailable"))
		
			else:
				frappe.msgprint(_(f"Book: {book_name} Issued"))
				#frappe.db.update('Books','self.book_name','book_status','Taken')
				frappe.db.set_value('Books',book_name,'book_status','Taken')

				doc=frappe.new_doc('Records')
				doc.member_name='self.member_name'
				doc.book='self.book_name'
				doc.date='datetime.today()'
				doc.trasncation_type='self.action_type'
				doc.insert()

 
        
		
		elif self.action_type.lower()=="return":
			frappe.db.set_value('Books',book_name,'book_status','Avaialble')
			frappe.msgprint(_(f"Book: {book_name} Returned"))
			doc=frappe.new_doc('Records')
			doc.member_name='self.member_name'
			doc.book='self.book_name'
			doc.date='datetime.today()'
			doc.trasncation_type='self.action_type'
			doc.insert()

	


