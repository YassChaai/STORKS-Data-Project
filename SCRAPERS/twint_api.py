from traitlets import All
import twint

c = twint.Config()

c.Search = "#futuremaman"
c.Limit = 10000000
c.Store_csv = True
c.Output = "tweets.csv"

twint.run.Search(c)