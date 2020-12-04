#from AreeApplicative import areeApplicative, nomiAreeApplicative, areeApp
import re
import os
import shutil
import sys

def traduciTabella(riga, righeTabella):
	riga = riga.replace('::TAB\n', '::TAB')
	riga = riga.replace('\n', ' |\n| ')
	riga = riga.replace('::TAB', '\n| ')
	
	numeroColonne = riga.count('|')
	if righeTabella == 2:
		riga = riga + '---' + '|----'*(numeroColonne-2) + '|\n| '
	return riga

def traduzioneCompleta(tipoDOC):
	print('Translating: ' + tipoDOC)
	documentiAS = sys.argv[1]
	documentiMD = sys.argv[2] + '/documenti-md'
	basepath = documentiAS + '/' + tipoDOC

	# Creazione cartelle di destinazione

	if not os.path.exists(documentiMD):
		os.makedirs(os.path.join(sys.argv[2], 'documenti-md'))
		#os.mkdir(documentiMD)
	if not os.path.exists(documentiMD + '/DOC/TA/B£AMO'):
		os.makedirs(os.path.join(documentiMD, 'DOC', 'TA', 'B£AMO'))
	if not os.path.exists(documentiMD + '/DOC_OPE/TA/B£AMO'):
		os.makedirs(os.path.join(documentiMD,'DOC_OPE', 'TA', 'B£AMO'))
	if not os.path.exists(documentiMD + '/DOC_VIS/TA/B£A'):
		os.makedirs(os.path.join(documentiMD, 'DOC_VIS', 'TA', 'B£A'))
	if not os.path.exists(documentiMD + '/DOC/V3/ASE'):
		os.makedirs(os.path.join(documentiMD, 'DOC' , 'V3', 'ASE'))
	if not os.path.exists(documentiMD + '/DOC_OPE/MB/SCP_SCH'):
		os.makedirs(os.path.join(documentiMD, 'DOC_OPE' , 'MB', 'SCP_SCH'))
	if not os.path.exists(documentiMD + '/DOC/OJ/FILE'):
		os.makedirs(os.path.join(documentiMD, 'DOC' , 'OJ', 'FILE'))
	if not os.path.exists(documentiMD + '/DOC/OG/OG'):
		os.makedirs(os.path.join(documentiMD, 'DOC', 'OG', 'OG'))
	if not os.path.exists(documentiMD + '/DOC/OJ/PGM'):
		os.makedirs(os.path.join(documentiMD, 'DOC', 'OJ', 'PGM'))
	if not os.path.exists(documentiMD + '/DOC/OG/TA'):
		os.makedirs(os.path.join(documentiMD, 'DOC', 'OG', 'TA'))
	if not os.path.exists(documentiMD + '/DOC/OG/V2'):
		os.makedirs(os.path.join(documentiMD, 'DOC', 'OG', 'V2'))
	if not os.path.exists(documentiMD + '/DOC/OG/V3'):
		os.makedirs(os.path.join(documentiMD, 'DOC', 'OG', 'V3'))
	if not os.path.exists(documentiMD + '/DOC/V2/LOCOS'):
		os.makedirs(os.path.join(documentiMD, 'DOC', 'V2', 'LOCOS'))
	if not os.path.exists(documentiMD + '/DOC/H6/NWS'):
		os.makedirs(os.path.join(documentiMD, 'DOC', 'H6', 'NWS'))
	if not os.path.exists(documentiMD + '/FAQ/TA/B£AMO'):
		os.makedirs(os.path.join(documentiMD,'FAQ', 'TA', 'B£AMO'))
	if not os.path.exists(documentiMD + '/GLO/TA/B£AMO'):
		os.makedirs(os.path.join(documentiMD,'GLO', 'TA', 'B£AMO'))
	if not os.path.exists(documentiMD + '/Altro'):
		os.makedirs(os.path.join(documentiMD,'Altro'))

	if os.path.exists(documentiAS + '/' + tipoDOC):
		for fileTxt in os.listdir(documentiAS + '/' + tipoDOC):
			if os.path.isfile(os.path.join(basepath, fileTxt)):

				if fileTxt == '00INDEX.TXT':
					shutil.copy2(documentiAS + '/' + tipoDOC + '/' + fileTxt, documentiMD + '/' + tipoDOC + '_' + fileTxt)
					continue

				with open(os.path.join(basepath, fileTxt), encoding='utf8', errors='ignore') as f: # Apro documento AS in lettura
					tabella = False
					righeTabella = 0
					appNTI = ''
					appNWS = ''

					if '.TXT' in fileTxt:
						filemd = fileTxt.replace('.TXT', '.md')
					else:
						filemd = fileTxt + '.md'
						
					with open(filemd, 'w', encoding='utf8') as f1: # Creo/Apro documento MD in scrittura
						titoloFile = filemd.replace('.md','')
						
						for line in f:

							if titoloFile == '00INDEX' and tipoDOC == 'DOC':
								print(line)

							if '::I.INC.MBR Fil' in line and 'Mem' in line: # Inclusione di altri documenti (come link)
								parametro = line.rsplit('Fil(')[1]
								parametro = parametro.rsplit(')')[0]
								fileName = line.rsplit('Mem(')[1]
								fileName = fileName.rsplit(')')[0]
								
								pathParametro = 'documenti-md/MB/' + parametro
								path = pathParametro  + '/' + fileName
								
								if parametro == 'DOC':
									path = 'documenti-md/DOC/TA/B£AMO/' + fileName
								elif parametro == 'DOC_OPE':
									path = 'documenti-md/DOC_OPE/TA/B£AMO/' + fileName
								elif parametro == 'DOC_VIS':
									path = 'documenti-md/DOC_VIS/TA/B£A/' + fileName
								elif parametro == 'DOC_SER':
									path = 'documenti-md/DOC/V3/ASE/' + fileName
								elif parametro == 'DOC_SCH':
									path = 'documenti-md/DOC_OPE/MB/SCP_SCH/' + fileName
								elif parametro == 'DOC_OGG':
									if fileName[:2] == 'F_':
										path = 'documenti-md/DOC/OJ/FILE/' + fileName.replace('F_','', 1)
									elif fileName[:3] == 'OG_':
										path = 'documenti-md/DOC/OG/OG/' + fileName.replace('OG_','', 1)
									elif fileName[:2] == 'P_':
										path = 'documenti-md/DOC/OJ/PGM/' + fileName.replace('P_','', 1)
									elif fileName[:3] == 'TA_':
										path = 'documenti-md/DOC/OG/TA/' + fileName.replace('TA_','', 1)
									elif fileName[:3] == 'V2_':
										path = 'documenti-md/DOC/OG/V2/' + fileName.replace('V2_','', 1)
									elif fileName[:3] == 'V3_':
										path = 'documenti-md/DOC/OG/V3/' + fileName.replace('V3_','', 1)
									elif fileName[:3] == 'LOA' or fileName[:7] == 'V2LOCOS':
										path = 'documenti-md/DOC/V2/LOCOS/' + fileName


								if os.path.exists(documentiAS + '/' + parametro):
									if parametro == 'DOC' or parametro == 'DOC_OGG': # Recupero descrizioni in file di indice
										with open(documentiAS + '/'+ parametro + '/00INDEX.TXT', 'r', encoding='latin1') as indice:
											for riga in indice:
												if fileName in riga:
													descrizione = riga[riga.find('- ')+2 : riga.find('  ')]
													line = '- [' + descrizione + '](' + path + ')\n'
													break
									else:
										for linkedFile in os.listdir(documentiAS + '/' + parametro): # Recupero descrizioni nel nome del file
											if fileName in linkedFile and '(' in linkedFile and len(fileName) == 6:
												if len(linkedFile.rsplit(' (')[0]) == 6:
													descrizione = linkedFile[8 : -1]
													line = '- [' + descrizione + '](' + path + ')\n'
											elif fileName in linkedFile and '(' in linkedFile and len(fileName) != 6: # Se il nome del file contiene la descrizione
												descrizione = linkedFile[linkedFile.find('(')+1 : linkedFile.find(')')]

												line = '- [' + descrizione + '](' + path + ')\n'
								'''						
								if os.path.exists(path):
									with open(path, 'r', encoding='utf8') as f2:
										for l in f2:
											f1.write(l)
									line = ''
							'''		
							if 'http' in line and 'K(' in line: # Conversione link esterni
								fileName = line.rsplit('K(')[1]
								fileName = fileName.rsplit(')')[0]
								line = '[' + fileName + '](' + fileName + ')\n'
							if '::DEC' in line and 'P(' in line and 'T(' in line and 'K(' in line: # Conversione link interni 
								tipo = line.rsplit('T(')[1]
								tipo = tipo.rsplit(')')[0]
								parametro = line.rsplit('P(')[1]
								parametro = parametro.rsplit(')')[0]
								codice = line.rsplit('K(')[1]
								codice = codice.rsplit(')')[0]

								pathParametro = 'documenti-md/' + tipo + '/' + parametro
								path = pathParametro + '/' + codice
								
								if parametro == 'DOC':
									path = 'documenti-md/DOC/TA/B£AMO/' + codice
								elif parametro == 'DOC_OPE':
									path = 'documenti-md/DOC_OPE/TA/B£AMO/' + codice
								elif parametro == 'DOC_VIS':
									path = 'documenti-md/DOC_VIS/TA/B£A/' + codice
								elif parametro == 'DOC_SER':
									path = 'documenti-md/DOC/V3/ASE/' + codice
								elif parametro == 'DOC_SCH':
									path = 'documenti-md/DOC_OPE/MB/SCP_SCH/' + codice
								elif parametro == 'DOC_OGG':
									if codice[:2] == 'F_':
										path = 'documenti-md/DOC/OJ/FILE/' + codice.replace('F_','', 1)
									elif codice[:3] == 'OG_':
										path = 'documenti-md/DOC/OG/OG/' + codice.replace('OG_','', 1)
									elif codice[:2] == 'P_':
										path = 'documenti-md/DOC/OJ/PGM/' + codice.replace('P_','', 1)
									elif codice[:3] == 'TA_':
										path = 'documenti-md/DOC/OG/TA/' + codice.replace('TA_','', 1)
									elif codice[:3] == 'V2_':
										path = 'documenti-md/DOC/OG/V2/' + codice.replace('V2_','', 1)
									elif codice[:3] == 'V3_':
										path = 'documenti-md/DOC/OG/V3/' + codice.replace('V3_','', 1)
									elif codice[:3] == 'LOA' or codice[:7] == 'V2LOCOS':
										path = 'documenti-md/DOC/V2/LOCOS/' + codice
									

								if os.path.exists(documentiAS + '/' + parametro): 
									if parametro == 'DOC' or parametro == 'DOC_OGG' or parametro == 'DOC_VIS' or parametro == 'DOC_SCH' or parametro == 'DOC_SER' or parametro == 'DOC_OPE': # Recupero descrizioni in file di indice 
										with open(documentiAS + '/'+ parametro + '/00INDEX.TXT','r', encoding='latin1') as indice:
											for riga in indice:
												if codice in riga:
													descrizione = riga[riga.find('- ')+2 : riga.find('  ')]
													line = '- [' + descrizione + '](' + path + ')\n'
													break
									else:
										for linkedFile in os.listdir(documentiAS + '/' + parametro): # Recupero descrizioni nel nome del file
											if codice in linkedFile and '(' in linkedFile and len(codice) == 6:
												if len(linkedFile.rsplit(' (')[0]) == 6:
													descrizione = linkedFile[8 : -1]
													line = '- [' + descrizione + '](' + path + ')\n'
											elif codice in linkedFile and '(' in linkedFile and len(codice) != 6: # Se il nome del file contiene la descrizione
												descrizione = linkedFile[linkedFile.find('(')+1 : linkedFile.find(')')]

												line = '- [' + descrizione + '](' + path + ')\n'

							if '::FIG' in line and 'P(' in line: # Conversione immagini  
								img = line.rsplit('P(')[1]
								img = img.rsplit(')')[0]
								titoloFile = titoloFile.rsplit(' (')[0]
								if(tipoDOC == 'DOC'):
									pathImmagine = 'https://doc.smeup.com/immagini/' + titoloFile + '/' + img.replace('£','X').replace(' ','%20') + '.png'
								else:
									pathImmagine = 'https://doc.smeup.com/immagini/MB' + tipoDOC + '-' + titoloFile + '/' + img.replace('£','X').replace(' ','%20') + '.png'
								line = '![' + img + '](' + pathImmagine + ')'
								line = line.replace('\n','')

							if line.endswith('+\n'):
								line = line.replace('+\n','')

							if '::TAB' in line: # Conversione Tabella
								tabella = True
							if '::TAB.END' in line:
								righeTabella = 0
								tabella = False

							if tabella:
								righeTabella += 1
								line = traduciTabella(line, righeTabella)
							
							if '*' in line : # Ignora il carattere * nella sintassi markdown se non è il primo della riga
								if line.startswith('*'):
									line = line.replace('*', '- ', 1)
								line = line.replace('*','\*')
							
							line = line.replace('#', '-') # Conversione elenco puntato
							line = line.replace('::T01', '#') # Conversione titoli                             
							line = line.replace('::T02', '##')
							line = line.replace('::T03', '###')
									
							if tipoDOC == 'DOC_NWS': # Estrazione applicazione di appartenenza
								if 'App="' in line:
									appNWS = line.rsplit('App="')[1]
									appNWS = appNWS.rsplit('"')[0]
							
							if tipoDOC == 'DOC_VOC':
								if 'Txt="' in line: # Aggiungo voce Glossario o FAQ
									txtGLO = line.rsplit('Txt="')[1]

									if '"' not in txtGLO: # Trick per righe ::VOC troncate
										nextline = next(f)
										txtGLO = txtGLO + nextline.rsplit('"')[0]
									else:
										txtGLO = txtGLO.rsplit('"')[0]
									
									line = '### **' + txtGLO + '**\n\n' # + line + '\n\n'
									
							
							line = line.replace('::TAB.END', '\n')
							line = line.replace('::PAR F(02)\n', '>')
							line = line.replace('::PAR F(02)', '>')
							line = line.replace('::PAR.END','')
							line = line.replace('::PAR L(NUM)', '')
							line = line.replace('::PAR L(PUN)', '')
													
							
							if '_h_' in line: # Conversione grassetto
								line = line.replace('_h_ ','**')
								line = line.replace(' _n_','**')
								line = line.replace('_h_','**')
								line = line.replace('_n_','**')
							if '_i_' in line: # Conversione corsivo
								line = line.replace('_i_','_')
								line = line.replace('_n_','_')    
							if '_u_' in line: # Conversione sottolineato
								line = line.replace('_u_','__')
								line = line.replace('_n_','__')
							if '_8_' in line: # Conversione citazione/comando
								line = line.replace('_8_','>')
								line = line.replace('_n_','')

							line = line.replace('_n_','')
							
							if 'http' not in line:
								line = line.replace(':', ' : ')

							f1.write(line)
			
					if ' (' in filemd:
						newName = filemd.rsplit(' (')[0] + '.md'
					else:
						newName = filemd

					# Rinomina dei file, lasciando solo il codice
					if tipoDOC == 'DOC':
						os.rename(filemd, documentiMD + '/' + tipoDOC + '/TA/B£AMO/' + newName)
					elif tipoDOC == 'DOC_OPE':
						os.rename(filemd, documentiMD + '/' + tipoDOC + '/TA/B£AMO/' + newName)
					elif tipoDOC == 'DOC_VIS':
						os.rename(filemd, documentiMD + '/DOC_VIS/TA/B£A/' + newName)
					elif tipoDOC == 'DOC_SER':
						os.rename(filemd, documentiMD + '/DOC/V3/ASE/' + newName)
					elif tipoDOC == 'DOC_SCH':
						os.rename(filemd, documentiMD + '/DOC_OPE/MB/SCP_SCH/' + newName)
					elif tipoDOC == 'DOC_OGG':
						if newName[:2] == 'F_':
							os.rename(filemd, documentiMD + '/DOC/OJ/FILE/' + newName.replace('F_','', 1))
						elif newName[:3] == 'OG_':
							os.rename(filemd, documentiMD + '/DOC/OG/OG/' + newName.replace('OG_','', 1))
						elif newName[:2] == 'P_':
							os.rename(filemd, documentiMD + '/DOC/OJ/PGM/' + newName.replace('P_','', 1))
						elif newName[:3] == 'TA_':
							os.rename(filemd, documentiMD + '/DOC/OG/TA/' + newName.replace('TA_','', 1))
						elif newName[:3] == 'V2_':
							os.rename(filemd, documentiMD + '/DOC/OG/V2/' + newName.replace('V2_','', 1))
						elif newName[:3] == 'V3_':
							os.rename(filemd, documentiMD + '/DOC/OG/V3/' + newName.replace('V3_','', 1))
						elif newName[:3] == 'LOA' or newName[:7] == 'V2LOCOS':
							os.rename(filemd, documentiMD + '/DOC/V2/LOCOS/' + newName)
						else:
							os.rename(filemd, documentiMD + '/Altro/' + newName) 
					elif tipoDOC == 'DOC_NWS':
						if appNWS != '':
							if appNWS == 'L':
								appNWS = 'LO'
							if appNWS == 'M':
								appNWS = 'M5'
							if appNWS == 'N':
								appNWS = 'NS'
							if appNWS == 'O':
								appNWS = 'OD'
							os.rename(filemd, documentiMD + '/DOC/H6/NWS/' + appNWS + '_' + newName.replace('NWS', '', 1))
						else:
							os.rename(filemd, documentiMD + '/DOC/H6/NWS/' + newName.replace('NWS', '', 1))
					elif tipoDOC == 'DOC_VOC':
						if '_FAQ' in filemd:
							os.rename(filemd, documentiMD + '/FAQ/TA/B£AMO/' + newName.replace('_FAQ','',1))
						elif '_GLO' in filemd:
							os.rename(filemd, documentiMD + '/GLO/TA/B£AMO/' + newName.replace('_GLO','',1))
						else:
							os.rename(filemd, documentiMD + '/Altro/' + newName)

	if os.path.exists(documentiMD + '/Altro'):
		shutil.rmtree(documentiMD + '/Altro')

			
if __name__ == "__main__":
	#try:
    traduzioneCompleta('DOC')
    traduzioneCompleta('DOC_VIS')
    traduzioneCompleta('DOC_OGG')
    traduzioneCompleta('DOC_SCH')
    traduzioneCompleta('DOC_OPE')
    traduzioneCompleta('DOC_SER')
    traduzioneCompleta('DOC_NWS')
    traduzioneCompleta('DOC_VOC')
	#except Exception:
	#	print("Traduzione Fallita...")
	



