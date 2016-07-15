from TeXiPy import *

if __name__ == '__main__':

    d = TeXiPyDoc()

    d.fname = 'DemoPDF'
    d.title = 'Demo of TeXiPy Functionality'
    d.author = 'Author\'s Name'

    d + Section('Section Example')
    d + Subsection('First Subsection Example: Paragraphs')

    d + Subsubsection('Left Aligned')
    p1 = Paragraph(just='l')
    p1.text = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus
     diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus
     sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora
     torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero.
    '''
    d + p1

    d + Subsubsection('Center Aligned')
    p2 = Paragraph(just='c')
    p2.text = p1.text
    d + p2

    d + Subsubsection('Right Aligned')
    p3 = Paragraph(just='r')
    p3.text = p1.text
    d + p3

    d + Subsection('Second Subsection Example: Equations')
    d.addPackage('amsmath')
    eq = Equation()
    eq + 'y &= x^{2} + 2x + 1'
    eq + '&= (x+1)^{2}'
    d + eq

    d + Subsection('Third Subsection Example: Images')
    d.addPackage('graphicx')
    i = Image('testim.png', caption='Test Image', width=1.0)
    d + i

    d.renderPDF(title=True)
