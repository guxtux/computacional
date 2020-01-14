unit Hilo;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls;

type
  THilo = class(TThread)
  public
    procedure repintar(sender: TImage);
    procedure actualizara(sender: TObject);
    procedure calcularxf(sender: TObject);
    procedure actualizarx(sender: TObject);
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
  p: array[1..20] of particula;
  h: extended;

implementation

procedure THilo.Execute;
begin
  salir := false;
  while not salir do
  begin
    synchronize(actualizara);
    synchronize(calcularxf);
    synchronize(repintar);
    synchronize(actualizarx);
  end;
end;

procedure THilo.repintar(sender: TImage);
var
  I, x, y: Integer;
begin
  sender.canvas.brush.color := clwhite;
  sender.canvas.FillRect(rect(1,1,400,400));
  for I := 1 to 20 do
  begin
    x := round(p[i].x*40);
    y := round(p[i].y*40);
    sender.Canvas.Brush.Color := clblue;
    sender.Canvas.Ellipse(rect(x - 20, y - 20, x + 20, y + 20));
    sender.Canvas.MoveTo(x,y);
    sender.Canvas.LineTo(x + round(p[i].vx*40), y + round(p[i].vy*40));
  end;
end;

procedure THilo.actualizara(sender: TObject);
var
  I: Integer;
begin
  for I := 1 to 20 do
  begin
    p[i].ax := 0;
    p[i].ay := 0;
    for j := 1 to 20 do
    begin
      if j<>i then
      begin
        dx1 := p[i].x - p[j].x;
        dy1 := p[i].x - p[j].x;
        r1 := sqrt(dx1*dx1 + dy1*dy1);
        dx2 := p[i].x + p[j].x - 20;
        dy2 := p[i].x + p[j].x - 20;
        r2 := sqrt(dx2*dx2 + dy2*dy2);
      end;
      if r1 < r2 then
      begin
        dx := dx1;
        dy := dy1;
        r := r1;
      end
      else
      begin
        dx := dx2;
        dy := dy2;
        r := r2;
      end;
      rf := 24 * (2/power(r,13) - 1/power(r,7));
      p[i].ax := p[i].ax + rf*dx/r;
      p[i].ay := p[i].ay + rf*dy/r;
    end;
  end;
end;

procedure THilo.calcularxf(sender: TObject);
var
  I: Integer;
begin
  for I := 1 to 20 do
  begin
    p[i].xf := 2*p[i].x - p[i].xi + p[i].ax*h*h;
    p[i].yf := 2*p[i].y - p[i].yi + p[i].ay*h*h;
  end;
end;

procedure THilo.actualizarx(sender: TObject);
begin
  p[i].xi := p[i].x;
  p[i].yi := p[i].y;
  p[i].x := p[i].xf;
  p[i].y := p[i].yf;
end;

procedure THilo.terminar;
begin
  salir := true;
end;

end.
