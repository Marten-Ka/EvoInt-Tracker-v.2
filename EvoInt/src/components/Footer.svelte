<script>
	import { goto } from '$app/navigation';

	import NavigationButton from './NavigationButton.svelte';
    import Button from './Button.svelte';
    import Icon from './Icon.svelte';

	function onHome() {
		goto('/');
	}
</script>

<footer>
    <div class="flex flex-col w-full justify-evenly">
        <div class="flex flex-row w-full justify-evenly">
            <div>
                <img src="Logo.png" alt="EvoInt-Logo" width="220px" on:click={onHome} />
                <p class="vikus">Vikus-Viewer</p>
                <p class="vikusinfo">Find out more about the Vikus-Viewer:</p>
                <Button href="https://vikusviewer.fh-potsdam.de/" text="Vikus-Viewer" size="0"/>
            </div>
            
            <!-- Hier jetzt wie auf der GitHub-Seite eine Matrix von Links erstellen -->
            <div class="mt-20 h-full">
                <div class="grid grid-cols-3 gap-x-32 gap-y-4">
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">Impressum</a>
                    </div>
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">Privacy Policy</a>
                    </div>
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">Terms</a>
                    </div>
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">About</a>
                    </div>
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">Contact</a>
                    </div>
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">Blog</a>
                    </div>
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">Careers</a>
                    </div>
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">Press</a>
                    </div>
                    <div>
                        <a href="https://vikusviewer.fh-potsdam.de/">Social Impact</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="flex flex-row w-full justify-center mt-5">
            <p>Copyright © EvoInt. All rights reserved.</p>
        </div>

        <div class="flex flex-row w-full justify-center mt-4 gap-4">
            <Icon icon="twitter" size="32px" stroke_width="1" color="#DDD" />
            <Icon icon="instagram" size="32px" stroke_width="1" color="#DDD" />
            <Icon icon="youtube" size="32px" stroke_width="1" color="#DDD" />
            <Icon icon="linkedin" size="32px" stroke_width="1" color="#DDD" />
            <Icon icon="github" size="32px" stroke_width="1" color="#DDD" />
            <!-- <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 273.5 222.3"
                width="30px">
                <path
                d="M273.5 26.3a109.77 109.77 0 0 1-32.2 8.8 56.07 56.07 0 0 0 24.7-31 113.39 113.39 0 0 1-35.7 13.6 56.1 56.1 0 0 0-97 38.4 54 54 0 0 0 1.5 12.8A159.68 159.68 0 0 1 19.1 10.3a56.12 56.12 0 0 0 17.4 74.9 56.06 56.06 0 0 1-25.4-7v.7a56.11 56.11 0 0 0 45 55 55.65 55.65 0 0 1-14.8 2 62.39 62.39 0 0 1-10.6-1 56.24 56.24 0 0 0 52.4 39 112.87 112.87 0 0 1-69.7 24 119 119 0 0 1-13.4-.8 158.83 158.83 0 0 0 86 25.2c103.2 0 159.6-85.5 159.6-159.6 0-2.4-.1-4.9-.2-7.3a114.25 114.25 0 0 0 28.1-29.1" 
                fill="rgb(149, 157, 165)"/>
            </svg>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 19.17 13.6"
                width="30px">
                <path
                d="M18.77 2.13A2.4 2.4 0 0 0 17.09.42C15.59 0 9.58 0 9.58 0a57.55 57.55 0 0 0-7.5.4A2.49 2.49 0 0 0 .39 2.13 26.27 26.27 0 0 0 0 6.8a26.15 26.15 0 0 0 .39 4.67 2.43 2.43 0 0 0 1.69 1.71c1.52.42 7.5.42 7.5.42a57.69 57.69 0 0 0 7.51-.4 2.4 2.4 0 0 0 1.68-1.71 25.63 25.63 0 0 0 .4-4.67 24 24 0 0 0-.4-4.69zM7.67 9.71V3.89l5 2.91z"
                fill="rgb(149, 157, 165)"/>
            </svg>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 19 18"
                width="30px">
                <path
                    d="M3.94 2A2 2 0 1 1 2 0a2 2 0 0 1 1.94 2zM4 5.48H0V18h4zm6.32 0H6.34V18h3.94v-6.57c0-3.66 4.77-4 4.77 0V18H19v-7.93c0-6.17-7.06-5.94-8.72-2.91z"
                    fill="rgb(149, 157, 165)"/>
            </svg>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 16 16"
                width="30px">
                <path
                    fill="rgb(149, 157, 165)"
                    d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z">
                </path>
            </svg> -->
        </div>

    </div>
</footer>

<style lang="postcss">
	footer {
		@apply font-evoint pt-12 pb-5 w-full h-full flex items-center gap-5 border-t border-white border-opacity-20 bg-gray-900 text-gray-200;
	}

    .vikus {
        @apply text-2xl font-bold
    }

    .vikusinfo {
        @apply text-xl font-mono text-gray-400 mb-4
    }

	img {
		@apply mb-10 hover:cursor-pointer;
	}

    a {
        @apply font-mono text-gray-300 hover:text-blue-500 underline
    }

    p {
        @apply text-gray-400
    }

</style>