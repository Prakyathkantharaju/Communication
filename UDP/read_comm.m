function data = read_comm(cli)
data = NaN;
if cli.BytesAvailable > 0
    while cli.BytesAvailable ~= 0
        temp_data = fread(cli,cli.BytesAvailable);
        recv_data= double(convertCharsToStrings(char(temp_data)));
        if isnan(recv_data)
            % data is a string
            recv_data = convertCharsToStrings(char(temp_data));
        end
        
%         flushinput(cli);
    end
    flushinput(cli);
    % storing only the last data
    data = recv_data;
end
end