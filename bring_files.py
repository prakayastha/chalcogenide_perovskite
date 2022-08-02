import os

compounds =['Ba2ZrS4_I4_mmm', 'Ba3Zr2S7_Cmmm', 'Ba3Zr2S7_P42_mnm']
#compounds = ['BaS2_C2_c', 'ZrS_P4_nmm', 'ZrS_Fm-3m', 'ZrS3_P2_1m', 'BaS3_P-421m', 'ZrS2_P-3m1', 'BaS_Fm-3m']

for i in compounds:
	os.chdir(i)
	os.system('mv ../%s_phonon_BS.pdf .'%i)
	os.chdir('../')
