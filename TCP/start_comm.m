function t = start_comm()
    % This the creates a client by default
    t = tcpip('localhost',5005);
    % uncomment the client
%     t = tcpip('localhost',5005,
    fopen(t)
    if t.BytesAvailable > 0
        data = fread(t,t.BytesAvailable);
        data = convertCharsToStrings(char(data));
    end
end