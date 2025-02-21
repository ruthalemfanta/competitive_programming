class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictt = {}
        
        for cp in cpdomains:
            parts = cp.split(" ")
            num = int(parts[0])  
            domain = parts[1] 
            
            domains = domain.split('.')  
            
            for i in range(len(domains)):
                subdomain = ".".join(domains[i:])  
                if subdomain in dictt:
                    dictt[subdomain] += num  
                else:
                    dictt[subdomain] = num  
        
        out = []
        for subdomain, count in dictt.items():
            out.append(str(count) + " " + subdomain)  
        
        return out
