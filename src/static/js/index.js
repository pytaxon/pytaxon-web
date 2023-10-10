const dropArea = document.getElementById('drop-area');
        const fileInput = document.getElementById('file-input');

        // Adicione um ouvinte de evento para o evento "dragover" para evitar que o navegador abra o arquivo diretamente.
        function handleDragOver(e) {
            e.preventDefault();
            dropArea.style.backgroundColor = '#f2f2f2';
        }

        dropArea.addEventListener('dragover', handleDragOver);
        fileInput.addEventListener('dragover', handleDragOver);

        // Ouvinte de evento para reverter a cor de fundo quando o usuário sair da área de drop.
        function handleDragLeave() {
            dropArea.style.backgroundColor = '#ffffff';
        }

        dropArea.addEventListener('dragleave', handleDragLeave);
        fileInput.addEventListener('dragleave', handleDragLeave);

        // Ouvinte de evento para processar os arquivos quando o usuário soltar na área de drop.
        dropArea.addEventListener('drop', (e) => {
            e.preventDefault();
            dropArea.style.backgroundColor = '#ffffff';
            const files = e.dataTransfer.files;
            // Faça o que você quiser com os arquivos aqui, por exemplo, envie-os para o servidor.
            console.log(files);
        });

        // Ouvinte de evento para abrir o seletor de arquivos quando o usuário clica na área de drop.
        dropArea.addEventListener('click', () => {
            fileInput.click();
        });

        // Ouvinte de evento para capturar o arquivo selecionado no seletor de arquivos.
        fileInput.addEventListener('change', () => {
            const files = fileInput.files;
            // Faça o que você quiser com os arquivos aqui.
            console.log(files);
        });