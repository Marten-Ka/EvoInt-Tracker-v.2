<script lang="ts">
	import { goto } from '$app/navigation';
	import Icon from '../../components/Icon.svelte';

	export let text: string;
	export let href: string;
	export let icon: string = 'arrow-right';

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
	<Icon {icon} size="48px" />
	<span class="mr-8" />
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
		@apply p-5 flex items-center bg-black bg-opacity-20 border-2 border-transparent hover:border-gray-800 hover:scale-110 rounded-lg text-gray-300 uppercase font-bold transition-all duration-300 select-none;
	}
	.letter {
		@apply p-0.5 text-5xl hover:scale-125 rounded-lg transition-all;
	}
</style>
