<script lang="ts">
	import { goto } from '$app/navigation';
	import Icon from './Icon.svelte';

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

  //let w = window.innerWidth.valueOf()
  let wSize = ""
  function giveSize() {
    if (w <= 640) {
      wSize = "24px";
    } else if (w < 768) {
      wSize = "28px";
    } else if (w <= 1024) {
      wSize = "32px";
    } else if (w <= 1280) {
      wSize = "40px";
    } else  {
      wSize = "20px";
    }
    return wSize
  }
</script>

<div id="content" on:click={onClick}>
	<Icon {icon} size="28px" />
	<span class="mr-4" />
	{#each letters as letter}
		{#if letter === ' '}
			<span class="mr-2" />
		{:else}
			<span class="letter">{letter}</span>
		{/if}
	{/each}
</div>

<style lang="postcss">
	#content {
		@apply p-5 flex items-center bg-black bg-opacity-20 border-2 border-transparent hover:border-gray-800 hover:scale-110 rounded-lg text-gray-300 md:uppercase md:font-bold transition-all duration-300 select-none;
	}
	.letter {
		@apply p-0.5 text-xs sm:text-lg md:text-xl lg:text-3xl xl:text-5xl xl:text-4xl 2xl:text-6xl rounded-lg transition-all flex flex-col;
	}
</style>
