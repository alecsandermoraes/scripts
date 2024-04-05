require 'optparse'
require 'net/http'

options = {}
basefile = File.basename(__FILE__)
OptionParser.new do |opts|
    opts.banner = "Usage: ruby #{basefile} [options]"

    opts.on("-rREMOTE", "--remote=REMOTE", "Remote File") do |remote|
        options[:remote] = remote 
    end 

    opts.on("-lLOCAL", "--local=LOCAL", "Local File") do |local|
        options[:local] = local 
    end 
end.parse! 

def download_file(remote, local)
    begin 
        uri = URI(remote)
        response = Net::HTTP.get_response(uri)]
        
        if response.code == '200'
            File.open(local, 'wb') do |output|
                output.write(response.body)
            end 

            return true 
        else 
            puts "Erro no Download"
            puts "Status Code: #{response.code}"
            return false 
        end 
    rescue StandardError => e 
        puts "Erro no Download: #{e.message}"
        return false 
    end 
end 

if options[:remote] && options[:local]
    if download_file(options[:remote], options[:local])
        puts "Download Concluído"
    else 
        puts "Erro no Download"
    end 
else 
    puts "Forneça os Argumentos Corretamente"
end 
