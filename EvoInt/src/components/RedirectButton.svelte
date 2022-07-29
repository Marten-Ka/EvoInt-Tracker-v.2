<script lang="ts">
	import { goto } from '$app/navigation';

	export let text: string;
	export let href: string;

	function onClick() {
		goto(href);
	}
</script>

<div id="content" on:click={onClick}>
	{text}
</div>

<style lang="postcss">
	#content {
		@apply p-5 flex justify-center items-center bg-black bg-opacity-20 border-2 border-transparent hover:border-gray-800 hover:scale-110 rounded-lg text-center text-sm  sm:text-base md:text-lg lg:text-xl xl:text-3xl 2xl:text-5xl text-gray-400 hover:text-gray-300 uppercase font-bold transition-all duration-300 select-none;
	}
</style>
