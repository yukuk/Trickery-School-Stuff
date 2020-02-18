program InfinitySaper;

const
  n = 10;

var
  polea: array[1..n, 1..n] of string;
  poleb: array[1..n, 1..n] of string;
  i, j, xxx, yyy, k, bombs, row, col, win: integer;
  go: boolean;

procedure bang;
begin
  xxx := random(10) + 1;
  yyy := random(10) + 1;
  if poleb[xxx, yyy] <> 'x' then poleb[xxx, yyy] := 'x'
  else bang;
end;

procedure open(r, c: integer);
var c1, c2, c3, c4, c5, c6, c7, c8: boolean;
begin
  if ((r >= 1) and (r <= n) and (c >= 1) and (c <= n) and (polea[r, c] <> poleb[r, c])) then
  begin
    if poleb[r, c] = 'x' then 
    begin
      writeln('Игра окончена! Вы проиграли!');
      go := false;
      polea[r, c] := poleb[r, c];
    end;
    if poleb[r, c] = '0' then 
    begin
      polea[r, c] := poleb[r, c];
      open(r, c + 1);
      open(r, c - 1);
      open(r + 1, c);
      open(r - 1, c);
      open(r - 1, c - 1);
      open(r - 1, c + 1);
      open(r + 1, c - 1);
      open(r + 1, c + 1);
    end;
    if ((poleb[r, c] = '1') or (poleb[r, c] = '2') or (poleb[r, c] = '3') or (poleb[r, c] = '4') or (poleb[r, c] = '5') or (poleb[r, c] = '6') or (poleb[r, c] = '7') or (poleb[r, c] = '8')) then
    begin
      polea[r, c] := poleb[r, c];
      
      c1 := true;
      c2 := true;
      c3 := true;
      c4 := true;
      c5 := true;
      c6 := true;
      c7 := true;
      c8 := true;
      
      if (r = 1) then
      begin
        c4 := false;
        c5 := false;
        c6 := false;
      end;
      
      if (c = 1) then
      begin
        c2 := false;
        c5 := false;
        c7 := false;
      end;
      
      if (r = n) then
      begin
        c3 := false;
        c7 := false;
        c8 := false;
      end;
      
      if (c = n) then
      begin
        c1 := false;
        c6 := false;
        c8 := false;
      end;
      
      if (c1 = true) then
      begin
        if poleb[r, c + 1] = '0' then open(r, c + 1);
      end;
      
      if (c2 = true) then 
      begin
        if poleb[r, c - 1] = '0' then open(r, c - 1); 
      end;
      
      if (c3 = true) then 
      begin
        if poleb[r + 1, c] = '0' then open(r + 1, c);
      end;
      
      if (c4 = true) then
      begin
        if poleb[r - 1, c] = '0' then open(r - 1, c);
      end;
      
      if (c5 = true) then 
      begin
        if poleb[r - 1, c - 1] = '0' then open(r - 1, c - 1);
      end;
      
      if (c6 = true) then 
      begin
        if poleb[r - 1, c + 1] = '0' then open(r - 1, c + 1);
      end;
      
      if (c7 = true) then
      begin
        if poleb[r + 1, c - 1] = '0' then open(r + 1, c - 1);
      end;
      
      if (c8 = true) then 
      begin
        if poleb[r + 1, c + 1] = '0' then open(r + 1, c + 1);
      end;
    end;
  end;
end;

begin
  //Формирование и вывод зрительского поля
  for i := 1 to n do 
  begin
    for j := 1 to n do 
    begin
      polea[i, j] := '.';
      write(polea[i, j]:2);
    end;
    writeln;
  end;
  writeln;
  
  //Формирование игрового поля
  for i := 1 to n do 
  begin
    for j := 1 to n do 
    begin
      poleb[i, j] := '.';
    end;
  end;
  
  //Ввод данных о количестве бомб
  write('Сколько мин расставить? -> ');
  readln(bombs);
  while ((bombs < 1) or (bombs >= (n * n))) do
  begin
    writeln('Количество бомб должно лежать в диапазоне от 1 до ', n * n - 1);
    write('Сколько мин расставить? -> ');
    readln(bombs);
  end;
  writeln;
  
  //Расстанова бомб
  for i := 1 to bombs do 
  begin
    bang;
  end;
  
  //Расстановка чисел
  for i := 2 to n - 1 do
  begin
    for j := 2 to n - 1 do
    begin
      k := 0;
      if poleb[i, j] <> 'x' then
      begin
        if poleb[i + 1, j + 1] = 'x' then k := k + 1;
        if poleb[i + 1, j] = 'x' then k := k + 1;
        if poleb[i + 1, j - 1] = 'x' then k := k + 1;
        if poleb[i, j + 1] = 'x' then k := k + 1;
        if poleb[i, j - 1] = 'x' then k := k + 1;
        if poleb[i - 1, j + 1] = 'x' then k := k + 1;
        if poleb[i - 1, j] = 'x' then k := k + 1;
        if poleb[i - 1, j - 1] = 'x' then k := k + 1;
        poleb[i, j] := k.ToString;
      end;  
    end;
  end;
  
  for j := 2 to n - 1 do
  begin
    k := 0;
    if poleb[1, j] <> 'x' then
    begin
      if poleb[1, j + 1] = 'x' then k := k + 1;
      if poleb[2, j] = 'x' then k := k + 1;
      if poleb[1, j - 1] = 'x' then k := k + 1;
      if poleb[2, j + 1] = 'x' then k := k + 1;
      if poleb[2, j - 1] = 'x' then k := k + 1;
      poleb[1, j] := k.ToString;
    end;
  end;
  
  for j := 2 to n - 1 do
  begin
    k := 0;
    if poleb[n, j] <> 'x' then
    begin
      if poleb[n, j + 1] = 'x' then k := k + 1;
      if poleb[n - 1, j] = 'x' then k := k + 1;
      if poleb[n, j - 1] = 'x' then k := k + 1;
      if poleb[n - 1, j + 1] = 'x' then k := k + 1;
      if poleb[n - 1, j - 1] = 'x' then k := k + 1;
      poleb[n, j] := k.ToString;
    end;  
  end;
  
  for i := 2 to n - 1 do
  begin
    k := 0;
    if poleb[i, 1] <> 'x' then
    begin
      if poleb[i + 1, 1] = 'x' then k := k + 1;
      if poleb[i, 2] = 'x' then k := k + 1;
      if poleb[i - 1, 1] = 'x' then k := k + 1;
      if poleb[i + 1, 2] = 'x' then k := k + 1;
      if poleb[i - 1, 2] = 'x' then k := k + 1;
      poleb[i, 1] := k.ToString;
    end;
  end;
  
  for i := 2 to n - 1 do
  begin
    k := 0;
    if poleb[i, n] <> 'x' then
    begin
      if poleb[i + 1, n] = 'x' then k := k + 1;
      if poleb[i, n - 1] = 'x' then k := k + 1;
      if poleb[i - 1, n] = 'x' then k := k + 1;
      if poleb[i + 1, n - 1] = 'x' then k := k + 1;
      if poleb[i - 1, n - 1] = 'x' then k := k + 1;
      poleb[i, n] := k.ToString;
    end;  
  end;
  
  k := 0;
  if poleb[1, 1] <> 'x' then
  begin
    if poleb[1, 2] = 'x' then k := k + 1;
    if poleb[2, 1] = 'x' then k := k + 1;
    if poleb[2, 2] = 'x' then k := k + 1;
    poleb[1, 1] := k.ToString;
  end;
  
  k := 0;
  if poleb[1, n] <> 'x' then
  begin
    if poleb[1, n - 1] = 'x' then k := k + 1;
    if poleb[2, n] = 'x' then k := k + 1;
    if poleb[2, n - 1] = 'x' then k := k + 1;
    poleb[1, n] := k.ToString;
  end;
  
  k := 0;
  if poleb[n, 1] <> 'x' then
  begin
    if poleb[n - 1, 1] = 'x' then k := k + 1;
    if poleb[n, 2] = 'x' then k := k + 1;
    if poleb[n - 1, 2] = 'x' then k := k + 1;
    poleb[n, 1] := k.ToString;
  end;
  
  k := 0;
  if poleb[n, n] <> 'x' then
  begin
    if poleb[n, n - 1] = 'x' then k := k + 1;
    if poleb[n - 1, n] = 'x' then k := k + 1;
    if poleb[n - 1, n - 1] = 'x' then k := k + 1;
    poleb[n, n] := k.ToString;
  end;
  
  //Основной игровой процесс
  go := true;
  while (go) do
  begin
    writeln('Введите номер строки и столбца соответственно.');
    repeat
      begin
        write('Введите корректные номера -> ');
        readln(row, col);
      end
    until ((row >= 1) and (row <= n) and (col >= 1) and (col <= n));
    writeln;
    open(row, col);
    win := 0;
    for i := 1 to n do 
    begin
      for j := 1 to n do 
      begin
        if polea[i, j] = '.' then win := win + 1;
        write(polea[i, j]:2);
      end;
      writeln;
    end;
    writeln;
    if win = bombs then
    begin
      go := false;
      writeln('Вы выиграли!');
    end;
  end;
  
end.

