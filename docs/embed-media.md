# Embed media

You can embed video or audio in the card.

If you checked autoplay or loop attribute, it would annoy you when editing the card. There are two ways to prevent this:

1. Install a [Disable autoplay in webview](https://ankiweb.net/shared/info/525094096) add-on.
2. Uncheck Ankidia options and manually add attributes using script tag below.
    ```html
    <script>
      var video = document.querySelector('video');
      if (video) {
        video.setAttribute('loop', '');
        video.setAttribute('autoplay', '');
      }
    
      var audio = document.querySelector('audio');
      if (audio) {
        audio.setAttribute('autoplay', '');
      }
    </script>
    ``` 
