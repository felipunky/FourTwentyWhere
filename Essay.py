import pywinauto.mouse

urlOne = "https://www.google.com.co/search?biw=1280&bih=635&ei=TQAsWseaJcrXmAHQ273YBg&q=az+seguros&oq=az+seguros&gs_l=psy-ab.3...665612.668298.0.668411.0.0.0.0.0.0.0.0..0.0....0...1.1.64.psy-ab..0.0.0....0._Qs4s56HkxM"
print('\n'.join(map(str,out)))
print(len(f))
SendKeys('{F6}' + i + '{ENTER}', with_spaces=True)
time.sleep(2)
pywinauto.mouse.double_click('left',(400, 450))
time.sleep(1)
pywinauto.mouse.double_click('left',(200, 300))
SendKeys('^t')
SendKeys('{F6}' + i + '{ENTER}', with_spaces=True)
time.sleep(2)
pywinauto.mouse.double_click('left',(400, 450))
time.sleep(1)
pywinauto.mouse.double_click('left',(200, 300))

