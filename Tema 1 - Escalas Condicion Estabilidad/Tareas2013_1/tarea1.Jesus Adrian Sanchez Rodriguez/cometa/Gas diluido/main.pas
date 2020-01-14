unit main;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls, math;

const
  N = 25;
  sn = 5;
  h = 0.01;

type
  TForm1 = class(TForm)
    Image1: TImage;
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Edit1: TEdit;
    Label1: TLabel;
    procedure Button4Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

  THilo = class(TThread)
  public
    procedure repintar;
    procedure actualizara;
    procedure calcularxf;
    procedure actualizarx;
    procedure actualizarv;
    function minabs(x1, x2: extended): extended;
  private
    salir: boolean;
  protected
    procedure Execute; override;
    procedure terminar;
  end;

  particula = record
    x, y: extended; //las coordenadas actuales de la particula
    xi, yi: extended; //las coordenadas anteriores de la particula
    xf, yf: extended; //las coordenadas posteriores de la particula
    vx, vy: extended; //las componentes de la velocidad de la particula
    ax, ay: extended; //las componentes de la aceleracion de la particula
  end;

var
  Form1: TForm1;
  corriendo: boolean;
  hilo1: THilo;
  p: array[1..N] of particula;

implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
var
  posicion: array[0..sn,0..sn] of boolean;
  x, y, i, j, cont: integer;
begin
  for i := 0 to sn do
  begin
    for j := 0 to sn do
    begin
      posicion[i,j] := false;
    end;
  end;
  cont := 1;
  while cont <= N do
  begin
    x := random(sn);
    y := random(sn);
    if posicion[x,y] = false then
    begin
      p[cont].x := (10/sn * x + 5/sn) + ((2*random()-1) * (5/sn - 0.5));
      p[cont].y := (10/sn * y + 5/sn) + ((2*random()-1) * (5/sn - 0.5));
      cont := cont + 1;
      posicion[x,y] := true;
    end;
  end;
  for i := 1 to N do
  begin
    p[i].vx := 2*random()-1;
    p[i].vy := (2*random()-1) * sqrt(1 - p[i].vx * p[i].vx);
  end;
  {p[1].x := 5.5;
  p[2].x := 8.5;
  p[1].y := 5.2;
  p[2].y := 5;
  p[1].vx := -5;
  p[2].vx := 1;
  p[1].vy := 0;
  p[2].vy := 0;}
  hilo1.actualizara;
  for i := 1 to N do
  begin
    p[i].xi := p[i].x - p[i].vx*h + p[i].ax*h*h/2;
    p[i].yi := p[i].y - p[i].vy*h + p[i].ay*h*h/2;
  end;
  hilo1.repintar;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  if corriendo = false then
  begin
    corriendo := true;
    hilo1 := Thilo.Create(false);
    button2.Caption := 'Parar'
  end
  else
  begin
    corriendo := false;
    hilo1.terminar;
    hilo1.Free;
    button2.Caption := 'Correr';
  end;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  close;
end;

procedure THilo.Execute;
begin
  salir := false;
  while not salir do
  begin
    synchronize(actualizara);
    synchronize(calcularxf);
    synchronize(actualizarv);
    synchronize(repintar);
    synchronize(actualizarx);
    //sleep(1);
  end;
end;

procedure THilo.repintar;
var
  I, x, y: Integer;
begin
  Form1.Image1.Canvas.brush.color := clwhite;
  form1.Image1.canvas.FillRect(rect(0,0,400,400));
  for I := 1 to N do
  begin
    x := round(p[i].x*40);
    y := round(p[i].y*40);
    form1.Image1.Canvas.Brush.Color := clblue;
    form1.Image1.Canvas.Ellipse(rect(x - 20, y - 20, x + 20, y + 20));
    form1.Image1.Canvas.MoveTo(x,y);
    form1.Image1.Canvas.LineTo(x + round(p[i].vx*40), y + round(p[i].vy*40));
  end;
end;

procedure THilo.actualizara;
var
  I, j: Integer;
  dx1, dy1, dx2, dy2, dx, dy, r, rf: extended;
begin
  for I := 1 to N do
  begin
    p[i].ax := 0;
    p[i].ay := 0;
    for j := 1 to N do
    begin
      if j<>i then
      begin
        dx1 := p[i].x - p[j].x;
        dy1 := p[i].y - p[j].y;
        if dx1 <> 0 then
        begin
          dx2 := (-1*dx1/abs(dx1)) * (10 - abs(dx1));
        end
        else
        begin
          dx2 := 0;
        end;
        if dy1 <> 0 then
        begin
          dy2 := (-1*dy1/abs(dy1)) * (10 - abs(dy1));
        end
        else
        begin
          dy2 := 0;
        end;
        dx := minabs(dx1, dx2);
        dy := minabs(dy1, dy2);
        r := sqrt(dx*dx + dy*dy);
        rf := 24 * (2/power(r,13) - 1/power(r,7));
        p[i].ax := p[i].ax + rf*dx/r;
        p[i].ay := p[i].ay + rf*dy/r;
      end;
    end;
  end;
end;

procedure THilo.calcularxf;
var
  I: Integer;
begin
  for I := 1 to N do
  begin
    p[i].xf := 2*p[i].x - p[i].xi + p[i].ax*h*h;
    p[i].yf := 2*p[i].y - p[i].yi + p[i].ay*h*h;
  end;
end;

procedure THilo.actualizarx;
var
  I: Integer;
begin
  for I := 1 to N do
  begin
    if p[i].xf > 10 then
    begin
      p[i].xi := p[i].x - 10;
      p[i].x := p[i].xf - 10;
    end
    else if p[i].xf < 0 then
    begin
      p[i].xi := p[i].x + 10;
      p[i].x := p[i].xf + 10;
    end
    else
    begin
      p[i].xi := p[i].x;
      p[i].x := p[i].xf;
    end;

    if p[i].yf > 10 then
    begin
      p[i].yi := p[i].y - 10;
      p[i].y := p[i].yf - 10;
    end
    else if p[i].yf < 0 then
    begin
      p[i].yi := p[i].y + 10;
      p[i].y := p[i].yf + 10;
    end
    else
    begin
      p[i].yi := p[i].y;
      p[i].y := p[i].yf;
    end;
  end;
end;

procedure THilo.actualizarv;
var
  I: Integer;
  sum: extended;
begin
  sum := 0;
  for I := 1 to N do
  begin
    p[i].vx := (p[i].xf - p[i].xi)/(2*h);
    p[i].vy := (p[i].yf - p[i].yi)/(2*h);
    sum := sum + sqrt(p[i].vx*p[i].vx + p[i].vy*p[i].vy);
  end;
  form1.Edit1.Text := floattostr(sum);
end;

function THilo.minabs(x1: Extended; x2: Extended): extended;
begin
  if abs(x1) < abs(x2) then
  begin
    minabs := x1;
  end
  else
  begin
    minabs := x2;
  end;
end;

procedure THilo.terminar;
begin
  salir := true;
end;

end.
