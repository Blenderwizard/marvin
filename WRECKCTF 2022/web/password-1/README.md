# password-1
## Solved By: [Blenderwizard](https://github.com/Blenderwizard)
## Worth: 130 points
## Total Solves: 342
## Solution

The `/api/output` route is unprotected. It doesn't take our password as a call to the api.

`app.py`

`@server.get('/') async def root(request):`
``` html
<link rel="stylesheet" href="/style.css" />
<div class="container">
    <form class="content">
        <input type="text" placeholder="Password..."/>
        <input type="submit" value="Login" />
    </form>
</div>
<script>
    const sha256 = async (message) => {
      const data = (new TextEncoder()).encode(message);
      const hashed = await crypto.subtle.digest('SHA-256', data);
      return Array.from(new Uint8Array(hashed))
        .map((b) => b.toString(16).padStart(2, '0'))
        .join('')
    }
    (() => {
      const form = document.querySelector('form');
      form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const input = document.querySelector('input[type="text"]');
        const hash = (
          '8c59346d674a352c' +
          'aa36c0cb808ec0dd' +
          '28ba42144f760c12' +
          '564663b610c9ce2d'
        );
        if (await sha256(input.value) === hash) {
          const flag = await (await fetch('/api/output')).text();  <!--here-->
          document.querySelector('.content').textContent = flag;
        } else {
          input.removeAttribute('style');
          input.offsetWidth;
          input.style.animation = 'shake 0.25s';
        }
      });
    })();
</script>
```

Navigating to `/api/output` gets us the flag.