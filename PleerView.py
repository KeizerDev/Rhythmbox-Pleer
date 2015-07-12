# - encoding: utf8
import rb

from gi.repository import GObject, Gio, Peas, Gtk, GdkPixbuf
from gi.repository import RB

class PleerView(RB.EntryView):
	def initialise(self, source):
		self.source = source
		self.append_column(RB.EntryViewColumn.TITLE, True)
		self.append_column(RB.EntryViewColumn.ARTIST, True)
		self.append_column(RB.EntryViewColumn.DURATION, True)
		self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
	
	# Called when a row (track) is double-ckicked
	def do_entry_activated(self, entry):
		if self.get_selected_entries()[0]:
			self.props.shell_player.play_entry(self.get_selected_entries()[0], self.source)
