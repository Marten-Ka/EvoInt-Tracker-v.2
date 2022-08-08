<script>
	import { goto } from '$app/navigation';
	import Icon from './Icon.svelte';

	function onHome() {
		goto('/');
	}
</script>

<footer>
	<div class="flex flex-col p-5 w-full">
		<div
			class="flex flex-col lg:flex-row xl:flex-row 2xl:flex-row w-full gap-1 lg:gap-5 justify-around"
		>
			<div class="flex flex-col  justify-center">
				<div class="flex  justify-center">
					<img src="/Logo.png" alt="EvoInt-Logo" width="220px" on:click={onHome} />
				</div>
				<div class="vikus">Vikus-Viewer</div>
				<div class="vikusinfo">Find out more about the Vikus-Viewer:</div>
				<div class="flex justify-center">
					<a
						href="https://vikusviewer.fh-potsdam.de/"
						style="text-decoration: none;"
						class=" p-5 flex w-max text-xl justify-center items-center bg-black bg-opacity-20 border-2 border-transparent hover:border-gray-800 hover:scale-110 rounded-lg text-gray-400 hover:text-gray-300 uppercase font-bold transition-all duration-300 select-none"
						size="0">Vikus-Viewer</a
					>
				</div>
			</div>

			<div class="mt-20 h-full flex justify-center">
				<div class="grid grid-cols-3 gap-y-4 gap-x-24 lg:gap-x-8 xl:gap-x-32">
					<div>
						<a href="/footer_links">Impressum</a>
					</div>
					<div>
						<a href="/footer_links">Privacy Policy</a>
					</div>
					<div>
						<a href="/footer_links">Terms</a>
					</div>
					<div>
						<a href="/footer_links">About</a>
					</div>
					<div>
						<a href="/footer_links">Contact</a>
					</div>
					<div>
						<a href="/footer_links">Careers</a>
					</div>
				</div>
			</div>
		</div>

		<div class="flex flex-row w-full justify-center mt-5">
			<p>Copyright © EvoInt. All rights reserved.</p>
		</div>

		<div class="flex flex-row w-full justify-center mt-4 gap-4">
			<a href="https://github.com/Marten-Ka/EvoInt-Tracker-v.2.git">
				<Icon icon="github" size="32px" stroke_width="1" color="#DDD" />
			</a>
		</div>
	</div>
</footer>

<style lang="postcss">
	footer {
		@apply font-evoint pt-12 pb-5 flex w-full h-full items-center gap-5 border-t border-white border-opacity-20 bg-gray-900 text-gray-200;
	}

	.vikus {
		@apply text-2xl font-bold flex justify-center;
	}

	.vikusinfo {
		@apply text-xl font-mono text-gray-400 mb-4 flex text-center  justify-center;
	}

	img {
		@apply mb-10 hover:cursor-pointer;
	}

	a {
		@apply font-mono text-gray-300 hover:text-blue-500 underline;
	}

	p {
		@apply text-gray-400;
	}
</style>
