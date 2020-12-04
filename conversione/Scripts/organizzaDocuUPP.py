import os

if not os.path.exists('documenti'):
    os.mkdir('documenti')
if not os.path.exists('documenti/DOC'):
    os.mkdir('documenti/DOC')
if not os.path.exists('documenti/DOC_OPE'):
    os.mkdir('documenti/DOC_OPE')
if not os.path.exists('documenti/DOC_VIS'):
    os.mkdir('documenti/DOC_VIS')
if not os.path.exists('documenti/GLO'):
    os.mkdir('documenti/GLO')
if not os.path.exists('documenti/NWS'):
    os.mkdir('documenti/NWS')
if not os.path.exists('documenti/FAQ'):
    os.mkdir('documenti/FAQ')

f = open("documenti/_sidebar.md", "w")
if len(os.listdir('documenti-md/DOC/TA/B£AMO/')) != 0:
    f.write("- [Documentazione Applicativa](documenti/DOC/_sidebar.md)\n")
if len(os.listdir('documenti-md/DOC_OPE/TA/B£AMO/')) != 0:
    f.write("- [Documentazione Operativa](documenti/DOC_OPE/_sidebar.md)\n")
if len(os.listdir('documenti-md/FAQ/TA/B£AMO/')) != 0:
    f.write("- [FAQ](documenti/FAQ/_sidebar.md)\n")
if len(os.listdir('documenti-md/GLO/TA/B£AMO/')) != 0:
    f.write("- [GLO](documenti/GLO/_sidebar.md)\n")
f.close()

open("documenti/DOC/_sidebar.md", 'w').close()
with open("documenti/DOC/_sidebar.md", "a", encoding='utf8') as f:
    f.write('# Documentazione Applicativa\n')
    for file in os.listdir('documenti-md/DOC/TA/B£AMO/'):
        nomefile = file.replace('.md','')
        titolo = nomefile
        with open('documenti-md/DOC_00INDEX.TXT', 'r', encoding='latin1') as indice:
            for riga in indice:
                if nomefile in riga:
                    titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                    titolo = titolo.replace('\'', '\\\'')
                    break
        f.write('- [' + titolo +'](documenti-md/DOC/TA/B£AMO/' + file +')\n')
    for file in os.listdir('documenti-md/DOC/V3/ASE/'):
        nomefile = file.replace('.md','')
        titolo = nomefile
        with open('documenti-md/DOC_SER_00INDEX.TXT', 'r', encoding='latin1') as indice:
            for riga in indice:
                if nomefile in riga:
                    titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                    titolo = titolo.replace('\'', '\\\'')
                    break
        f.write('- [' + titolo +'](documenti-md/DOC/V3/ASE/' + file +')\n')

open("documenti/DOC_OPE/_sidebar.md", 'w').close()
with open("documenti/DOC_OPE/_sidebar.md", "a", encoding='utf8') as f:
    f.write('# Documentazione Operativa\n')
    for file in os.listdir('documenti-md/DOC_OPE/TA/B£AMO/'):
        nomefile = file.replace('.md','')
        titolo = nomefile
        with open('documenti-md/DOC_OPE_00INDEX.TXT', 'r', encoding='latin1') as indice:
            for riga in indice:
                if nomefile in riga:
                    titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                    titolo = titolo.replace('\'', '\\\'')
                    break
        f.write('- [' + titolo +'](documenti-md/DOC_OPE/TA/B£AMO/' + file +')\n')
    for file in os.listdir('documenti-md/DOC_OPE/MB/SCP_SCH/'):
        nomefile = file.replace('.md','')
        titolo = nomefile
        with open('documenti-md/DOC_SCH_00INDEX.TXT', 'r', encoding='latin1') as indice:
            for riga in indice:
                if nomefile in riga:
                    titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                    titolo = titolo.replace('\'', '\\\'')
                    break
        f.write('- [' + titolo +'](documenti-md/DOC_OPE/MB/SCP_SCH/' + file +')\n')

open("documenti/FAQ/_sidebar.md", 'w').close()
with open("documenti/FAQ/_sidebar.md", "a", encoding='utf8') as f:
    f.write('# FAQ\n')
    for file in os.listdir('documenti-md/FAQ/TA/B£AMO/'):
        nomefile = file.replace('.md','')
        titolo = nomefile
        with open('documenti-md/DOC_VOC_00INDEX.TXT', 'r', encoding='latin1') as indice:
            for riga in indice:
                if nomefile in riga:
                    titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                    titolo = titolo.replace('\'', '\\\'')
                    break
        f.write('- [' + titolo +'](documenti-md/FAQ/TA/B£AMO/' + file +')\n')

open("documenti/GLO/_sidebar.md", 'w').close()
with open("documenti/GLO/_sidebar.md", "a", encoding='utf8') as f:
    f.write('# GLO\n')
    for file in os.listdir('documenti-md/GLO/TA/B£AMO/'):
        nomefile = file.replace('.md','')
        titolo = nomefile
        with open('documenti-md/DOC_VOC_00INDEX.TXT', 'r', encoding='latin1') as indice:
            for riga in indice:
                if nomefile in riga:
                    titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                    titolo = titolo.replace('\'', '\\\'')
                    break
        f.write('- [' + titolo +'](documenti-md/GLO/TA/B£AMO/' + file +')\n')
