from AreeApplicative import nomiDOC, nomiDOC_OPE, applicazioni, areeApplicative, nomiAreeApplicative, areeApp, moduli, nomiDOC_SCH, nomiDOC_OGG, nomiDOC_NWS, nomiDOC_SER, nomiDOC_NTI, nomiFAQ, nomiGLO, moduliDOC_OPE
import os

dataFile = os.path.abspath('data.js')
basepath = 'documenti-md'
basepath1 = 'documenti'
with open(dataFile, "w",  encoding='utf8') as f: 
    f.write('var data = [\n')
    f.write('\n')
    cont = 0
    for dirname, dirnames, filenames in os.walk(basepath):
        #print(dirname)
        for singleFile in filenames:
            nomefile = singleFile.replace('.md', '')
            path = os.path.join(dirname,singleFile)
            
            f.write('{\n')
            f.write('id: ' + str(cont) + ",\n")
            
            if 'OJ\\FILE' in dirname:
                nomefile = 'F_' + nomefile
                with open('documenti-md/DOC_OGG_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_OGG",\n')
                #f.write('voci: "",\n')
            elif 'OJ\\PGM' in dirname:
                nomefile = 'P_' + nomefile
                with open('documenti-md/DOC_OGG_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_OGG",\n')
                #f.write('voci: "",\n')
            elif 'OG\\OG' in dirname:
                nomefile = 'OG_' + nomefile
                with open('documenti-md/DOC_OGG_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_OGG",\n')
                #f.write('voci: "",\n')
            elif 'OG\\TA' in dirname:
                nomefile = 'TA_' + nomefile
                with open('documenti-md/DOC_OGG_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_OGG",\n')
                #f.write('voci: "",\n')
            elif 'OG\\V2' in dirname:
                nomefile = 'V2_' + nomefile
                with open('documenti-md/DOC_OGG_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_OGG",\n')
                #f.write('voci: "",\n')
            elif 'OG\\V3' in dirname:
                nomefile = 'V3_' + nomefile
                with open('documenti-md/DOC_OGG_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_OGG",\n')
                #f.write('voci: "",\n')
            elif 'V2\\LOCOS' in dirname:
                with open('documenti-md/DOC_OGG_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_OGG",\n')
                #f.write('voci: "",\n')
            elif 'DOC\\TA' in dirname:
                with open('documenti-md/DOC_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_APP",\n')
                #f.write('voci: "",\n')
            elif 'DOC_OPE\\TA' in dirname:
                with open('documenti-md/DOC_OPE_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_OPE",\n')
                #f.write('voci: "",\n')
            elif 'FAQ' in dirname:
                nomefile = nomefile + '_FAQ'
                with open('documenti-md/DOC_VOC_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "FAQ",\n')
                #f.write('voci: "",\n')
            elif 'GLO' in dirname:
                with open(os.path.join(dirname,singleFile), "r",  encoding='utf8') as f1: 
                    voci = []
                    for line in f1:
                        if 'Txt="' in line:
                            txtGLO = line.rsplit('Txt="')[1]
                            txtGLO = txtGLO.rsplit('"')[0]
                            voci.append(txtGLO)
                nomefile = nomefile + '_GLO'
                with open('documenti-md/DOC_VOC_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "GLO",\n')
                f.write('voci: "')
                for voce in voci:
                    f.write(voce + ' ')
                f.write('",\n')
            elif 'NWS' in dirname:
                with open(os.path.join(dirname,singleFile), "r",  encoding='utf8') as f1: 
                    rel = ''
                    num = ''
                    for line in f1:
                        if 'Rel="' in line:
                            rel = line.rsplit('Rel="')[1]
                            rel = rel.rsplit('"')[0]
                        if 'Num="' in line:
                            num = line.rsplit('Num="')[1]
                            num = num.rsplit('"')[0]
                nomefile = nomefile.replace('_', '_NWS')
                with open('documenti-md/DOC_NWS_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "NWS",\n')
                f.write('rel: "' + rel + '",\n')
                f.write('num: "' + num + '",\n')
            elif 'MB\\SCP_SCH' in dirname:
                with open('documenti-md/DOC_SCH_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_SCH",\n')
                #f.write('voci: "",\n')
            elif 'V3\\ASE' in dirname:
                with open('documenti-md/DOC_SER_00INDEX.TXT', 'r', encoding='latin1') as indice:
                    for riga in indice:
                        if nomefile in riga:
                            titolo = riga[riga.find('- ')+2 : riga.find('  ')]
                            titolo = titolo.replace('\'', '\\\'')
                            break
                f.write('title: \'' + titolo + '\',\n')
                f.write('cat: "DOC_SER",\n')
                #f.write('voci: "",\n')
            elif 'TA\\B£A' in dirname:
                if nomefile in applicazioni:
                    f.write('title: "' + applicazioni[nomefile] + '",\n')
                    f.write('cat: "DOC_VIS",\n')
                    #f.write('voci: "",\n')
                else:
                    f.write('title: "",\n')
                    f.write('cat: "",\n')
                    #f.write('voci: "",\n')
            else:
                f.write('title: "",\n')
                f.write('cat: "",\n')
                #f.write('voci: "",\n')

            f.write('href: "' + path.replace('\\', '/') + '"\n},')
            cont = cont + 1

    for dirname, dirnames, filenames in os.walk(basepath1):
        #print(dirname)
        for singleFile in filenames:
            nomefile = singleFile.replace('.md', '')
            path = os.path.join(dirname,singleFile)
            # print(path)

            f.write('{\n')
            f.write('id: ' + str(cont) + ",\n")

            if 'DOC\\DOC_APP' in dirname:
                for key, value in areeApp.items():
                    if key in dirname:
                        if dirname.endswith(key):
                            f.write('title: "' + value + '",\n')
                            f.write('cat: "Indice DOC_APP",\n')
                            # f.write('voci: "",\n')
                        for codice, nome in applicazioni.items():
                            if codice in dirname:
                                f.write('title: "' + nome + '",\n')
                                f.write('cat: "Indice DOC_APP",\n')
                                # f.write('voci: "",\n')
            elif 'DOC\\DOC_SER' in dirname:
                for key, value in areeApp.items():
                    if key in dirname:
                        if dirname.endswith(key):
                            f.write('title: "' + value + '",\n')
                            f.write('cat: "Indice DOC_SER",\n')
                            #f.write('voci: "",\n')
                        for codice, nome in applicazioni.items():
                            if codice in dirname:
                                f.write('title: "' + nome + '",\n')
                                f.write('cat: "Indice DOC_SER",\n')
                                #f.write('voci: "",\n')
            elif 'DOC_VIS' in dirname:
                for key, value in areeApp.items():
                    if key in dirname:
                        if dirname.endswith(key):
                            f.write('title: "' + value + '",\n')
                            f.write('cat: "Indice DOC_VIS",\n')
                            #f.write('voci: "",\n')
                        for codice, nome in applicazioni.items():
                            if codice in dirname:
                                f.write('title: "' + nome + '",\n')
                                f.write('cat: "Indice DOC_VIS",\n')
                                #f.write('voci: "",\n')
            elif 'DOC_OPE' in dirname:
                for key, value in areeApp.items():
                    if key in dirname:
                        if dirname.endswith(key):
                            f.write('title: "' + value + '",\n')
                            f.write('cat: "Indice DOC_OPE",\n')
                            #f.write('voci: "",\n')
                        for codice, nome in applicazioni.items():
                            if codice in dirname:
                                f.write('title: "' + nome + '",\n')
                                f.write('cat: "Indice DOC_OPE",\n')
                                #f.write('voci: "",\n')
            elif 'FAQ' in dirname:
                for key, value in areeApp.items():
                    if key in dirname:
                        if dirname.endswith(key):
                            f.write('title: "' + value + '",\n')
                            f.write('cat: "Indice FAQ",\n')
                            #f.write('voci: "",\n')
                        for codice, nome in applicazioni.items():
                            if codice in dirname:
                                f.write('title: "' + nome + '",\n')
                                f.write('cat: "Indice FAQ",\n')
                                #f.write('voci: "",\n')
            elif 'GLO' in dirname:
                for key, value in areeApp.items():
                    if key in dirname:
                        if dirname.endswith(key):
                            f.write('title: "' + value + '",\n')
                            f.write('cat: "Indice GLO",\n')
                            #f.write('voci: "",\n')
                        for codice, nome in applicazioni.items():
                            if '\\' + codice in dirname:
                                f.write('title: "' + nome + '",\n')
                                f.write('cat: "Indice GLO",\n')
                                #f.write('voci: "",\n')
            elif 'NWS\\News' in dirname:
                for key, value in areeApp.items():
                    if key in dirname:
                        if dirname.endswith(key):
                            f.write('title: "' + value + '",\n')
                            f.write('cat: "Indice NWS",\n')
                            #f.write('voci: "",\n')
                        for codice, nome in applicazioni.items():
                            if '\\' + codice in dirname:
                                f.write('title: "' + nome + '",\n')
                                f.write('cat: "Indice NWS",\n')
                                #f.write('voci: "",\n')
            else:
                f.write('title: "",\n')
                f.write('cat: "",\n')
                #f.write('voci: "",\n')

            f.write('href: "' + path.replace('\\', '/') + '"\n},')
            cont = cont + 1

    f.write('];')

