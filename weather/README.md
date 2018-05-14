# rewrite of the weather server
## To create an offline weather file that is quickly (re)created

The main concept is as follows:
1. take data from online ressource (same as original)
2. generate weather_records --> skip mysql/java
3. generate forecasts in parallel with some matrix magic in python


```
mysql> SHOW COLUMNS FROM forecasts;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| weatherDate | datetime     | NO   | PRI | NULL    |       |
| origin      | datetime     | NO   | PRI | NULL    |       |
| location    | varchar(256) | NO   | PRI | NULL    |       |
| temp        | float        | NO   |     | NULL    |       |
| windSpeed   | float        | NO   |     | NULL    |       |
| windDir     | int(11)      | NO   |     | NULL    |       |
| cloudCover  | float        | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+

mysql> SHOW COLUMNS FROM reports
    -> ;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| weatherDate | datetime     | NO   | PRI | NULL    |       |
| location    | varchar(256) | NO   | PRI | NULL    |       |
| temp        | float        | NO   |     | NULL    |       |
| windSpeed   | float        | NO   |     | NULL    |       |
| windDir     | int(11)      | NO   |     | NULL    |       |
| cloudCover  | float        | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
```

```
package org.powertac.weatherserver.beans;

public class Forecast extends Weather {
  private int id = 0;
  private String origin;

}


public class Weather {
	private String weatherDate;
  private String location;

	private Double temp;
	private Double windDir;
	private Double windSpeed;
	private Double cloudCover;

	public Weather ()
  {
		weatherDate = "0000000000";
		temp = 0.0;
		windDir = 0.0;
		windSpeed = 0.0;
		cloudCover = 0.0;
		location = "NONE";
	}
}

```
