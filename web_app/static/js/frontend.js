const F = {
    getFirstChildByTag: (parent, tag) => {
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
                const img = F.getFirstChildByTag(elems[i], 'IMG');
                if (!img) continue;
                elems[i].style.backgroundImage = `url('${img.src}')`;
                elems[i].title = img.alt;
                for (const [key, value] of Object.entries(options)) {
                    elems[i].style[key] = value;
                }
                img.remove()
            }
        }
    },
    Modal: {
        make: (title, body, buttons, noCloseBtn = false, appendToDocument = false, modalId = null) => {
            const modalDiv = document.createElement('div');
            modalDiv.classList.add('modal', 'fade');
            modalDiv.tabIndex = '-1';
            modalDiv.setAttribute('aria-hidden', 'true');
            const modalDialog = document.createElement('div');
            modalDialog.classList.add('modal-dialog');
            const modalContent = document.createElement('div');
            modalContent.classList.add('modal-content');
            const modalHeader = document.createElement('div');
            modalHeader.classList.add('modal-header');
            const modalTitle = document.createElement('h5');
            modalTitle.classList.add('modal-title');
            modalTitle.innerHTML = title;
            let closeButton;
            if (!noCloseBtn) {
                closeButton = document.createElement('button');
                closeButton.type = 'button';
                closeButton.classList.add('btn-close');
                closeButton.setAttribute('data-bs-dismiss', 'modal');
                closeButton.setAttribute('aria-label', 'Close');
            }
            const modalBody = document.createElement('div');
            modalBody.classList.add('modal-body');
            modalBody.innerHTML = body;
            const modalFooter = document.createElement('div');
            modalFooter.classList.add('modal-footer');
            modalHeader.appendChild(modalTitle);
            buttons.forEach(btn => modalFooter.appendChild(btn));
            if (closeButton) modalHeader.appendChild(closeButton);
            if (modalId) modalDiv.id = modalId;
            modalContent.appendChild(modalHeader);
            modalContent.appendChild(modalBody);
            modalContent.appendChild(modalFooter);
            modalDialog.appendChild(modalContent);
            modalDiv.appendChild(modalDialog);
            if (appendToDocument) document.body.appendChild(modalDiv);
            return modalDiv;
        },
        makeBootstrapModal: (title, body, buttons, noCloseBtn = false, modalId = null,onDismissCb, autoDispose = true,staticBackdrop = false) =>{
            const modalDiv = F.Modal.make(title,body,buttons,noCloseBtn,true,modalId);
            const genericModal = staticBackdrop ? new bootstrap.Modal(modalDiv, {
                backdrop: 'static'
              }) : new bootstrap.Modal(modalDiv);
          
          
              modalDiv.addEventListener('hidden.bs.modal', evt => {
                if (onDismissCb) {
                  onDismissCb(evt);
                }
                if (autoDispose) {
                  genericModal.dispose();
                  modalDiv.remove();
                }
              });
          
              return genericModal;
        }
    }
}