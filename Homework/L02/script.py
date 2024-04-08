import lxml.html


counter = {
    "Owais Nginx Server1!": 0,
    "Owais Nginx Server2!": 0,
    "Owais Nginx Server3!": 0,
    "Owais Nginx Server4!": 0,
}
63
print(counter)
for i in range(2000):
    t = lxml.html.parse("http://ec2-3-145-116-158.us-east-2.compute.amazonaws.com")
    title = t.find(".//title").text
    counter[title]+=1
    

print("=== Usage Statistics ===")
for key in counter: 
    print("Server Name: ", key, '--- TOTAL VISITS: ', counter[key])
