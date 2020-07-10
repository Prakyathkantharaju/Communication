        
function t = start_comm()
% t = udpclient('localhost', 22222);
t = udp('localhost', 'RemotePort', 4096, 'LocalPort', 5005);
% cli = tcpip('localhost', 50001, 'NetworkRole', 'client');
fopen(t);
% fwrite(t,'START');
if t.BytesAvailable > 0
    data = fread(t,t.BytesAvailable);
    data = convertCharsToStrings(char(data))
end
% fopen(cli);
end