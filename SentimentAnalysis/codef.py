def domainAuction(websites):
    domains = []
    domainCount = {}
    for website in websites:
        i = 0
        while website[i:i + 3] != '://':
            i += 1
        i += 3
        while i < len(website) and website[i] != '/':
            i += 1
        j = i - 1
        cnt = 0
        while website[j] != '/':
            cnt += 1 if website[j] == '/' or website[j] == '.' else 0
            if cnt == 2:
                break
            j -= 1
        domain = website[j + 1 : i]
        domains.append(domain)
        if domain not in domainCount:
            domainCount[domain] = 0
        domainCount[domain] += 1
    counts = []
    for domain in domains:
        counts.append(domainCount[domain])
    return counts

print domainAuction(["http://codefights.com",
 "https://uk.domainmaster.com",
 "https://uk.domainmaster.com/websites/website-builder",
 "https://in.domainmaster.com"])
