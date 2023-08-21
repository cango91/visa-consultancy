const F = {
    _getFirstChildByTag: (parent,tag) => {
        let child = parent.firstElementChild;
        while (child) {
            if (child.tagName === tag.toUpperCase()) {
              return child;
            }
            child = child.nextElementSibling;
          }
          return null; // If no matching child is found
    },
    Parallax: {
        init: (elems, options = {} = {
            minHeight: '500px',
        }) => {
            elems = Array.from(elems);
            for (let i = 0; i < elems.length; i++) {
                const img = F._getFirstChildByTag(elems[i],'IMG');
                if(!img) continue;           
                elems[i].style.backgroundImage = `url('${img.src}')`;
                elems[i].title = img.alt;
                for(const [key,value] of Object.entries(options)){
                    elems[i].style[key] = value;
                }
                img.remove()
            }
        }
    }
}