from calais import Calais
API_KEY="dkm645ejqmq7aajt8cp6zxk7"
calais = Calais(API_KEY, submitter="python-calais demo")
result = calais.analyze("My 15 year old Daughter has sores in her genital area and her mouth.She swares she did nothing but kiss her boyfriend.She also has flu-like symptoms.")
result.print_summary()
result.print_entities()
result.print_topics()
p=raw_input()