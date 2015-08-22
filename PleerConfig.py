import rb
from gi.repository import GObject, Gio, GLib, Peas, Gtk, PeasGtk
from gi.repository import RB

class PleerConfig(GObject.Object, PeasGtk.Configurable):
	_gtype_name_ = 'PleerConfig'
	object = GObject.property(type=GObject.Object)
	
	def do_create_configure_widget(self):
		schema_src = Gio.SettingsSchemaSource.new_from_directory(self.plugin_info.get_module_dir(), Gio.SettingsSchemaSource.get_default(), False)
		schema = schema_src.lookup('org.gnome.rhythmbox.plugins.pleer', False)
		self.settings = Gio.Settings.new_full(schema, None, None)
		
		self.builder = Gtk.Builder()
		self.builder.add_from_file(self.plugin_info.get_module_dir() + '/ui/pleer-prefs.ui')
		
		self.dir_dl = self.builder.get_object('dir_download_string')
		
		self.dir_dl.connect('changed', self.on_dirDownloadString_changed)
		self.settings.bind('dir-download-string', self.dir_dl, 'text', Gio.SettingsBindFlags.GET)
		
		content = self.builder.get_object('pleer-prefs')

		return content
	
	def on_dirDownloadString_changed(self, widget):
		self.settings.set_string('dir-download-string', self.dir_dl.get_text())
	

GObject.type_register(PleerConfig)