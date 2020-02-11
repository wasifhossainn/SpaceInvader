# -*- mode: python -*-

block_cipher = None


a = Analysis(['mainmenu2.py'],
             pathex=['C:\\Users\\Luka Jakovljevic\\Desktop\\Master Space Invaders'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mainmenu2',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')
