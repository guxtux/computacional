object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Form1'
  ClientHeight = 419
  ClientWidth = 903
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object marco: TImage
    Left = 8
    Top = 8
    Width = 800
    Height = 400
  end
  object traza: TImage
    Left = 8
    Top = 8
    Width = 800
    Height = 400
    Visible = False
  end
  object Button1: TButton
    Left = 814
    Top = 64
    Width = 75
    Height = 25
    Caption = 'Iniciar'
    TabOrder = 0
    OnClick = Button1Click
  end
  object Button2: TButton
    Left = 814
    Top = 104
    Width = 75
    Height = 25
    Caption = 'Ver Traza'
    TabOrder = 1
    OnClick = Button2Click
  end
end
