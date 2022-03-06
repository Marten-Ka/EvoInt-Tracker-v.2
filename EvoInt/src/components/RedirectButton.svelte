<script lang="ts">
	import { goto } from '$app/navigation';

	export let text: string;
	export let href: string;

	let letters: string[] = [];
	$: {
		letters = [];
		for (let i = 0; i < text.length; i++) letters.push(text.charAt(i));
	}

	function onClick() {
		goto(href);
	}
</script>

<div id="content" on:click={onClick}>
	{#each letters as letter}
		{#if letter === ' '}
			<span class="mr-8" />
		{:else}
			<span class="letter">{letter}</span>
		{/if}
	{/each}
</div>

<style lang="postcss">
	#content {
		@apply p-5 flex justify-center items-center bg-black bg-opacity-20 border-2 border-transparent hover:border-gray-800 hover:scale-110 rounded-lg text-gray-400 hover:text-gray-300 uppercase font-bold transition-all duration-300 select-none;
	}
	.letter {
		@apply p-0.5 text-6xl hover:scale-125 rounded-lg transition-all;
	}
</style>
