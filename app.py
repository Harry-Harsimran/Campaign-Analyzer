from flask import Flask, render_template, request
import analytics as an

app = Flask(__name__)


@app.route("/")
def overview():
    df = an.load()
    return render_template("overview.html", k=an.kpis(df),
                           monthly=an.by_month(df), channels=an.by_channel(df))


@app.route("/channels")
def channels():
    df = an.load()
    return render_template("channels.html", channels=an.by_channel(df), types=an.by_type(df))


@app.route("/campaigns")
def campaigns():
    df = an.load()
    channel = request.args.get("channel", "")
    ctype = request.args.get("type", "")
    sort = request.args.get("sort", "ROI")
    desc = request.args.get("dir", "desc") == "desc"
    rows = an.campaigns(df, channel, ctype, sort, desc)
    return render_template("campaigns.html", rows=rows, sort=sort, desc=desc,
                           channel=channel, ctype=ctype,
                           channel_opts=sorted(df["channel"].unique()),
                           type_opts=sorted(df["campaign_type"].unique()))


if __name__ == "__main__":
    app.run(debug=True)
