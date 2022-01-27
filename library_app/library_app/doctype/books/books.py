# Copyright (c) 2022, Priyatosh and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _


class Books(Document):
    
    def validate(self):
        self.set_value()

    def set_value(self):
        doc1=frappe.db.get_value('Books','Naruto Manga Part1','book_name')
        frappe.msgprint(_(f"{doc1}"))

    
   
      