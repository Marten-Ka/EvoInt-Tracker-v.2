<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import { goto } from '$app/navigation';

	const dispatch = createEventDispatcher();

	export let text: string;
	export let size: string;
	export let href: string;

	function onClick() {
		goto(href);
	}
</script>

<button on:click={onClick} class={'button-' + size}>{text}</button>

<style lang="postcss">
	.button-0 {
		@apply p-5 flex text-xl justify-center items-center bg-black bg-opacity-20 border-2 border-transparent hover:border-gray-800 hover:scale-110 rounded-lg text-gray-400 hover:text-gray-300 uppercase font-bold transition-all duration-300 select-none;
	}
	.button-1 {
		@apply p-5 flex text-4xl justify-center items-center bg-black bg-opacity-20 border-2 border-transparent hover:border-gray-800 hover:scale-110 rounded-lg text-gray-400 hover:text-gray-300 uppercase font-bold transition-all duration-300 select-none;
	}
	.button-2 {
		@apply p-5 flex text-7xl justify-center items-center bg-black bg-opacity-20 border-2 border-transparent hover:border-gray-800 hover:scale-110 rounded-lg text-gray-400 hover:text-gray-300 uppercase font-bold transition-all duration-300 select-none;
	}
</style>
