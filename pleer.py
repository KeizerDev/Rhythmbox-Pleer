import rb

from gi.repository import GObject, Gio, Peas, Gtk, GdkPixbuf
from gi.repository import RB

from PleerSource import PleerSource
from PleerFunctions import getMp3URL

class PleerEntryType(RB.RhythmDBEntryType):
	def __init__(self):
		RB.RhythmDBEntryType.__init__(self, name='pleer')

	def do_can_sync_metadata(self, entry):
		return True

	def do_get_playback_uri(self, entry):
		pleerFileLink = entry.dup_string(RB.RhythmDBPropType.LOCATION)
		mp3URL = getMp3URL(pleerFileLink)

		return(mp3URL)

class Pleer(GObject.Object, Peas.Activatable):
	gtype_name = 'Pleer'
	object = GObject.property(type=GObject.GObject)

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		shell = self.object
		db = shell.props.db
		model = RB.RhythmDBQueryModel.new_empty(db)
		entry_type = PleerEntryType()
		db.register_entry_type(entry_type)
		what, width, height = Gtk.icon_size_lookup(Gtk.IconSize.LARGE_TOOLBAR)
		# iconfile = Gio.File.new_for_path(self.plugin_info.get_data_dir()+"/icon.ico")
		iconfile = Gio.File.new_for_path(self.plugin_info.get_data_dir()+"/vk-symbolic.svg")
		source_group = RB.DisplayPageGroup.get_by_id("library")
		self.source = GObject.new(PleerSource, name=_("Pleer"), shell=shell, query_model=model, plugin=self, entry_type=entry_type, icon=Gio.FileIcon.new(iconfile))
		shell.append_display_page(self.source, source_group)
		shell.register_entry_type_for_source(self.source, entry_type)
		self.source.initialise()

def do_deactivate(self):
	self.source.delete_thyself()
	self.source = None
