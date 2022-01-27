# Copyright (c) 2022, Priyatosh and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _


class LibraryMembers(Document):

	'''
	def validate(self):
		self.get_document()

	def get_document(self):
		doc=frappe.get_doc('Library Members',self.member_full_name)
		frappe.msgprint(_(f"Data: {doc}"))	

	

	def new_document(self):
		doc=frappe.new_doc('Books')
		doc.books_name="MR  KUMAR"
		doc.books_author="MR  KUMAR"
		doc.books_publisher="MR  KUMAR"
		doc.save()

	def validate(self):
		self.new_document()

	'''