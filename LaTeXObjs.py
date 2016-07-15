class LaTeXObj(object):

    def __init__(self):
        self.commands = []

    def __str__(self):
        for command in self.commands:
            print command

    def __finalize__(self):
        self.addCommands()

########################################################################################################################
# Itemize, Enumerate, etc.
########################################################################################################################


class Itemize(LaTeXObj):

    def __init__(self, nosep=False):
        super(Itemize, self).__init__()
        self.items = []
        self.nosep = nosep

    def __add__(self, other):
        self.items.append(other)

    def addItem(self, item):
        self.items.append(item)

    def addCommands(self):

        if self.nosep:
            self.commands.append('\\begin{itemize}[noitemsep]')
        else:
            self.commands.append('\\begin{itemize}')

        for item in self.items:
            self.commands.append('\\item %s' % item)

        self.commands.append('\\end{itemize}')



class Enumerate(LaTeXObj):

    def __init__(self, nosep=False):
        super(Enumerate, self).__init__()
        self.items = []
        self.nosep = nosep

    def __add__(self, other):
        self.items.append(other)

    def addItem(self, item):
        self.items.append(item)

    def addCommands(self):

        self.commands.append('\\begin{enumerate}')

        for item in self.items:
            self.commands.append('\\item %s' % item)

        self.commands.append('\\end{enumerate}')

########################################################################################################################
# Images
########################################################################################################################

class Image(LaTeXObj):

    def __init__(self, impath, caption=None, width=0.5, justify='h'):

        super(Image, self).__init__()

        self.impath = impath
        self.caption = caption
        self.justify = justify
        self.width = width

    def addCommands(self):

        self.commands.append("\\begin{figure}[%s]" % self.justify)

        if self.caption != None:
            self.commands.append("\\caption{%s}" % self.caption)

        self.commands.append("\\centering")
        self.commands.append("\\includegraphics[width=%s\\textwidth]{%s}" %(self.width,self.impath))
        self.commands.append("\\end{figure}")

########################################################################################################################
# Paragraphs
########################################################################################################################

class Paragraph(LaTeXObj):

    def __init__(self, just='l', spacing=1):

        super(Paragraph,self).__init__()
        self.text = ''
        self.just = just
        self.spacing = spacing
        self.justification = {'c': 'centering', 'l': 'flushleft', 'r': 'flushright'}

    def addCommands(self):
        self.commands.append("\\begin{%s}" %(self.justification[self.just]))
        self.commands.append(self.text + '\\\\')
        self.commands.append("\\end{%s}" %(self.justification[self.just]))


########################################################################################################################
# Add Sections, Subsections, etc.
########################################################################################################################

class Section(LaTeXObj):

    def __init__(self, sectName, numbered=True):
        super(Section, self).__init__()
        self.sectName = sectName
        self.numbered = numbered

    def addCommands(self):
        if self.numbered:
            self.commands.append("\\section{%s}" % self.sectName)
        else:
            self.commands.append("\\section*{%s}" % self.sectName)

class Subsection(LaTeXObj):

    def __init__(self, subsectName, numbered=True):
        super(Subsection, self).__init__()
        self.subsectName = subsectName
        self.numbered = numbered

    def addCommands(self):
        if self.numbered:
            self.commands.append("\\subsection{%s}" % self.subsectName)
        else:
            self.commands.append("\\subsection*{%s}" % self.subsectName)



class Table(LaTeXObj):

    def __init__(self, array, ):
        super(Table, self).__init__()
        self.array = array
        self.rows = len(array)
        self.cols = len(array[0])


    def addCommands(self):
        self.commands.append("\\begin{center}")
        self.commands.append("\\begin{tabular}{|%s}" %(self.rows*' c |'))
        self.commands.append("\\hline")
        for row in self.array:
            row_command = ''
            for col in row[:-1]:
                row_command += "%s &" % col
            row_command += "%s \\\\ \\hline" %row[-1:][0]
            self.commands.append(row_command)

        self.commands.append("\\end{tabular}")
        self.commands.append("\\end{center}")


class Equation(LaTeXObj):

    def __init__(self):
        super(Equation, self).__init__()
        self.lines = []

    def __add__(self, other):
        self.lines.append(other)

    def addCommands(self):
        self.commands.append("\\begin{equation*}")
        self.commands.append("\\begin{split}")
        for line in self.lines:
            self.commands.append(line + ' \\\\')
        self.commands.append("\\end{split}")
        self.commands.append("\\end{equation*}")
