Title: Django regroup template tag
Date: 2012-05-27 18:53
Tags: django, template, python, web-development
Category: programming
Slug: django-regroup-tag
Summary: Use the template system power for grouping the request output data, in an example web framework like Django.

It is a common problem, the case in which we have a huge dictionary, with several fields with repeated data among those dictionary entries. Printing the dictionary, entry by entry, is going to show those repeated field values, and sometimes is not really cool. For a better visualization, we can think that is better to group the entries with the same field value, and we don't know how to do it in the template side.

## We can do more in the template

What is the regroup template tag? It will helps us to loop through a data structure, grouping each entry by a desired field, or maybe we want to group more than once.

It is a bit tricky to understand this issue so let's put an example. For instance, we have a `gps` points list where each of it has `latitude`, `longitude` and a `date`. The date is a `datetime` object (let's think about it like `year + month +  day`, though it has an hour and the representation of that object is a bit different). Then, we want to organize those points by `year`, `month` and `day`.

For instance, we will have a link per `day` to another page, showing with detail all the gps points for that specific day. Those days are grouped by months, and the months by years. Both months and years values will redirect to a page filtering the entries.

A possible approach to this problem would be the following piece of code (arranged in a table), where `points` is the variable list provided by the view:

    :::css+django
    {% regroup points by date|date:"Y" as points_by_year %}
    <div class="entry-content">
        {% for year_points in points_by_year %}
        <table>
            <caption>
                {{year_points.grouper}}
            </caption>
            {% regroup year_points.list by date|date:"M" as points_by_month %}
            {% for month_points in points_by_month %}
            <tr>
                <td>
                    <p>{{month_points.grouper}}</p>
                    {% regroup month_points.list by date|date:"d" as points_by_day %}
                    {% for day_points in points_by_day %}
                    <p>
                        <a href="{% url nextpage_name year_points.grouper month_points.grouper day_points.grouper %}">
                            {{day_points.grouper}}
                        </a>
                    </p>
                    {% endfor %}
                </td>
            </tr>
            {% endfor %}
        </table>
        {% endfor %}
    </div>

The `grouper` variable will show the string of the item that was grouped by, and if it was by year, then it is the year value, because we have filtered it like this:

    :::css+django
    {% regroup points by date|date:"Y" as points_by_year %}

Using the following piece of code is another way of creating the url for the next page. We need to specify the `nextpage_name` in `urls.py` and the other two strings are the arguments, so the server will know what page to show.

    :::css+django
    {% url nextpage_name year_points.grouper month_points.grouper day_points.grouper %}

## Let's see how it looks

The result should be something like this:

![Regrouping tag overview](http://i.imgur.com/fILp6.png)

We don't really need the `latitude` and `longitude` here, but we need to know that we have X points for a specific day, to show only the involved days. We can create a set of tables where each table is a single year. At the end, it is very simple and there are other solutions, but this is one of them, using the powerful Django regroup template tag. You can browse more information about these tags in the [Django Documentation](https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs).

## Other template languages

This guide can be applied to other template languages like `Jinja2`. There is a great explanation in the [Jinja2 Documentation](http://jinja.pocoo.org/docs/templates/#groupby), and is pretty similar to the `Django` approach.