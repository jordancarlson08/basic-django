
class Table(list):
	'''Custom Bootstrap Paginated Table'''

	## --- Overwrite these variables --- ##
	headings = [ 'Column 1', 'Column 2' ]
	endpoint = '/homepage/table.get_table/pagenum/'
	rows_per_page = 25

	def __init__(self, qry, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.qry = qry

	def paginate(self, request):
		try:
			page = int(request.urlparams[0])
		except ValueError:
			page = 0

		self.qry = self.qry[page * self.rows_per_page: (page + 1) * self.rows_per_page]


	def __str__(self):
		html = []
		html.append('<table class="table table-bordered table-striped">')

		## ---- Headers ---- ##
		html.append('<thead>')
		html.append('<tr>')
		for head in self.headings:
			html.append('<th>{}</th>'.format(head))
		html.append('</tr>')
		html.append('</thead>')

		## ---- Body ---- ##
		html.append('<tbody>')
		for row in self:
			html.append('<tr>')
			for item in row:
				html.append('<td>{}</td>'.format(item))
			html.append('</tr>')
		html.append('</tbody>')


		html.append('</table>')
		return ''.join(html)