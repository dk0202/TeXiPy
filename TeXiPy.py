from subprocess import call
from LaTeXObjs import *



########################################################################################################################
########################################################################################################################

class TeXiPyDoc:
    def __init__(self):
        self.fname = None
        self.title = None
        self.author = None
        self.packages = []
        self.head = []
        self.body = []

    def __add__(self, other):
        self.body.append(other)

    def __finalize__(self):
        for obj in self.body:
            if type(obj) != str:
                obj.__finalize__()

    def addPackage(self, pname):
        self.packages.append(pname)


    def docStructure(self):
        for obj in self.body:
            print type(obj)

    ####################################################################################################################
    # TeX Compilation and PDF Rendering
    ####################################################################################################################

    def generateHead(self):
            self.head.append("\\documentclass{article}\n")
            self.head.append("\\usepackage[utf8]{inputenc}\n")
            self.head.append("\\title{%s}\n"%self.title)
            self.head.append("\\author{%s}\n"%self.author)

    def produceTeX(self, title=False):

        with open("%s.tex" % self.fname, 'w') as f:

            self.__finalize__()

            self.generateHead()
            for line in self.head:
                f.write(line)

            for package in self.packages:
                f.write("\\usepackage{%s}\n"%package)

            f.write("\\begin{document}\n")

            if title:
                f.write("\\maketitle\n")

            for obj in self.body:
                for command in obj.commands:
                    f.write(command+'\n')

            f.write("\\end{document}\n")

        f.close()

    def renderPDF(self, title=False):
        self.produceTeX(title=title)
        call(['pdflatex', "%s.tex" % self.fname])


########################################################################################################################
########################################################################################################################
