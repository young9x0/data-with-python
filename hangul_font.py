from matplotlib import font_manager, rc
import platform

def to_hangul_font():
  if platform.system() == 'Windows':
    path='c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname= path).get_name()
    rc('font',family= font_name)
  elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
  else:
    print('check your os system')

