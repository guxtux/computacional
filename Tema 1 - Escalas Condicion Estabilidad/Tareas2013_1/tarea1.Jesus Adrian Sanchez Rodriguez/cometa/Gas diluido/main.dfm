object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Form1'
  ClientHeight = 484
  ClientWidth = 525
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Image1: TImage
    Left = 8
    Top = 8
    Width = 400
    Height = 400
  end
  object Label1: TLabel
    Left = 412
    Top = 196
    Width = 17
    Height = 13
    Caption = 'K ='
  end
  object Button1: TButton
    Left = 432
    Top = 33
    Width = 75
    Height = 25
    Caption = 'Inicializar'
    TabOrder = 0
    OnClick = Button1Click
  end
  object Button2: TButton
    Left = 432
    Top = 64
    Width = 75
    Height = 25
    Caption = 'Correr'
    TabOrder = 1
    OnClick = Button2Click
  end
  object Button3: TButton
    Left = 432
    Top = 95
    Width = 75
    Height = 25
    Caption = 'Cambiar'
    TabOrder = 2
  end
  object Button4: TButton
    Left = 432
    Top = 126
    Width = 75
    Height = 25
    Caption = 'Salir'
    TabOrder = 3
    OnClick = Button4Click
  end
  object Edit1: TEdit
    Left = 432
    Top = 192
    Width = 75
    Height = 21
    TabOrder = 4
  end
end
