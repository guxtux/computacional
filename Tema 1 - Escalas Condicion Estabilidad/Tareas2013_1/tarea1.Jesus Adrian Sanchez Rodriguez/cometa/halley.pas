unit halley;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls, Math;

type
    TFuerza = record
    x,y:extended;
  end;

  TForm1 = class(TForm)
    marco: TImage;
    Button1: TButton;
    traza: TImage;
    Button2: TButton;
    procedure Button1Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    function funcionFuerza(x,y:extended):TFuerza;
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

  TAnimacion = class(TThread)
      procedure actualizar;
    private
      salir: boolean;
    protected
      procedure Execute; override;
      procedure terminar;
  end;

  TFuncionFuerza = function(xf,yf:extended):TFuerza of object;

  TCuerpo = class(TObject)
      dt:extended;//delta t del algoritmo de verlet
      vx,vy:extended;//velocidad del cuerpo
      vtx,vty:extended;//velocidad del cuerpo en medio paso
      acx,acy:extended;//aceleracion del cuerpo
      fuerza:TFuncionFuerza;
      x,y:extended;//posicion del cuerpo
      procedure llenar(dti,xi,yi,vxi,vyi:extended;fuerzai:TFuncionFuerza);
      procedure verlet();
  end;
var
  Form1: TForm1;
  corriendo, verTraza: boolean;
  animacion: TAnimacion;
  cometaHalley: TCuerpo;

implementation

{$R *.dfm}

{ TAnimacion }

procedure TAnimacion.actualizar;
var
  x,y:integer;
begin
  cometaHalley.verlet;
  x := Form1.marco.Width-50+integer(round(cometaHalley.x*20));
  y := (Form1.marco.Height div 2)-integer(round(cometaHalley.y*20));
  Form1.marco.Canvas.Brush.Color := clwhite;
  Form1.marco.Canvas.FillRect(Rect(0,0,Form1.marco.Width,Form1.marco.Height));
  Form1.marco.Canvas.Brush.Color := clblack;
  Form1.marco.Canvas.Ellipse(x-2,y-2,x+2,y+2);
  Form1.marco.Canvas.Brush.Color := clyellow;
  Form1.marco.Canvas.Ellipse(Form1.marco.Width-55,Form1.marco.Height div 2-5,Form1.marco.Width-45,Form1.marco.Height div 2+5);
  //Form1.traza.Canvas.Brush.Color := clwhite;
  //Form1.traza.Canvas.FillRect(Rect(0,0,Form1.traza.Width,Form1.traza.Height));
  //Form1.traza.Canvas.Brush.Color := clyellow;
  //Form1.traza.Canvas.Ellipse(Form1.traza.Width-55,Form1.traza.Height div 2-5,Form1.traza.Width-45,Form1.traza.Height div 2+5);
  Form1.traza.Canvas.Pen.Color := clblack;
  Form1.traza.Canvas.LineTo(x,y);
end;

procedure TAnimacion.Execute;
begin
  inherited;
  salir:=false;
  while not salir do
  begin
    synchronize(actualizar);
    //sleep(1);
  end;
end;

procedure TAnimacion.terminar;
begin
  salir:=true;
end;

{ TCuerpo }

procedure TCuerpo.llenar(dti,xi, yi, vxi, vyi: extended; fuerzai: TFuncionFuerza);
begin
  x:=xi;
  y:=yi;
  dt:=dti;
  vx:=vxi;
  vy:=vyi;
  fuerza:=fuerzai;
  acx:=fuerza(x,y).x;
  acy:=fuerza(x,y).y;
end;

procedure TCuerpo.verlet;
begin
  vtx := vx + 0.5*acx*dt;
	vty := vy + 0.5*acy*dt;
	x := x + vtx*dt;
	y := y + vty*dt;
	acx := fuerza(x,y).x;
	acy := fuerza(x,y).y;
	vx := vtx + acx*dt;
	vy := vty + acy*dt;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  if corriendo then
  begin
    corriendo := false;
    animacion.terminar;
    animacion.Free;
    button1.Caption := 'Iniciar';
  end
  else
  begin
    corriendo := true;
    animacion := TAnimacion.Create(false);
    button1.Caption := 'Detener';
  end;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  if verTraza then
  begin
    traza.Visible := false;
    marco.Visible := true;
    button2.Caption := 'Ver Traza';
    verTraza := false;
  end
  else
  begin
    marco.Visible := false;
    traza.Visible := true;
    button2.Caption := 'Ver Cometa';
    verTraza := true;
  end;
end;

procedure TForm1.FormCreate(Sender: TObject);
var
  x,y: integer;
begin
  corriendo := false;
  verTraza := false;
  cometaHalley := TCuerpo.Create;
  cometaHalley.llenar(0.0001,-35.1,0,0,-9.12,Form1.funcionFuerza);
  x := marco.Width-50+round(cometaHalley.x*20);
  y := marco.Height div 2-round(cometaHalley.y*20);
  marco.Visible := true;
  traza.Visible := false;
  marco.Canvas.Brush.Color := clwhite;
  marco.Canvas.FillRect(Rect(0,0,marco.Width,marco.Height));
  marco.Canvas.Brush.Color := clblack;
  marco.Canvas.Ellipse(x-2,y-2,x+2,y+2);
  marco.Canvas.Brush.Color := clyellow;
  marco.Canvas.Ellipse(marco.Width-55,marco.Height div 2-5,marco.Width-45,marco.Height div 2+5);
  traza.Canvas.Brush.Color := clwhite;
  traza.Canvas.FillRect(Rect(0,0,traza.Width,traza.Height));
  traza.Canvas.Brush.Color := clyellow;
  traza.Canvas.Ellipse(marco.Width-55,marco.Height div 2-5,marco.Width-45,marco.Height div 2+5);
  traza.Canvas.Pen.Color := clblack;
  traza.Canvas.Pen.Style := psSolid;
  traza.Canvas.MoveTo(x,y);
end;

function TForm1.funcionFuerza(x, y: extended): TFuerza;
var
  fuerzas: TFuerza;
begin
  fuerzas.x:= -x*50000/power(x*x+y*y, 1.5);
  fuerzas.y:= -y*50000/power(x*x+y*y, 1.5);
  Result := fuerzas;
end;

end.
